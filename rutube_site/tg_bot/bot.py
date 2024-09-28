import os
import sys
import django
import random
import requests
import warnings
warnings.filterwarnings('ignore')
from collections import defaultdict
import requests
import aiohttp
from aiohttp.client_exceptions import ClientConnectorError
import json
from asgiref.sync import sync_to_async

import pandas as pd
from env import API_TOKEN, TOKEN_TRANSFORMRS_API

# Добавляем путь к директории с проектом
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Задаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rutube_app.settings')

django.setup()

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from gradio_client import Client
from chat_bot.models import QueryAnswer
from pydub import AudioSegment

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Загрузка модели для работы с эмбеддингами
base_dir = os.path.dirname(os.path.abspath(__file__))

# Поднимаемся на один уровень выше
parent_dir = os.path.dirname(base_dir)
print(parent_dir)
model_path = os.path.join(parent_dir, "tg_bot", "models")
os.makedirs(model_path, exist_ok=True)

# Инициализация модели эмбеддингов
model = SentenceTransformer(model_path)

# # Загрузка данных из базы данных
faq_data = QueryAnswer.objects.all()
faq_data_dict = {item.query: item.answer for item in faq_data}

# Создание эмбеддингов для заголовков
titles = [item.query for item in faq_data]
print("Длина titles", len(titles))

print("Создаём и нормализуем эмбендинги")
title_embeddings = model.encode(titles)
title_embeddings = normalize(title_embeddings)
print("Готов к работе!")


# Функция для поиска наиболее релевантного ответа
def find_best_match(query: str):
    similarity_threshold = 0.6  # Пороговое значение для сходства
    # Преобразование запроса пользователя в эмбеддинг
    user_query_embedding = model.encode([query])
    user_query_embedding = normalize(user_query_embedding)

    # Поиск наиболее релевантного заголовка
    title_similarity_scores = cosine_similarity(user_query_embedding, title_embeddings)
    # print(title_similarity_scores)
    best_title_idx = title_similarity_scores.argmax()
    if title_similarity_scores[0][best_title_idx] < similarity_threshold:
        print("Ответ не найден, сходство слишком низкое.")
        return None, None
    

    # Получение наиболее подходящего заголовка и контента
    best_match_title = titles[best_title_idx]
    best_match_content = faq_data_dict.get(best_match_title, None)
    
    return best_match_title, best_match_content


async def generate_detailed_response(query: str, best_match_content: str, best_match_title: str):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3:8b",
        "prompt": f"Пользователь задал вопрос: '{query}'. Сгенерируйте подробный и полезный ответ на основании: | Содержание - {best_match_content} и Заголовок - {best_match_title}."
    }

    full_response = ""  # Переменная для накопления ответа

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                # Чтение NDJSON построчно
                async for line in response.content:
                    decoded_line = line.decode('utf-8').strip()  # Декодируем и очищаем строку
                    if decoded_line:
                        try:
                            # Попытка преобразовать строку в JSON
                            json_data = json.loads(decoded_line)
                            # Добавляем фрагмент ответа к полному ответу
                            full_response += json_data.get('response', '')
                            # Если ответ завершен, выходим из цикла
                            if json_data.get('done', False):
                                break
                        except json.JSONDecodeError:
                            print("Ошибка декодирования JSON:", decoded_line)
            else:
                print(f"Ошибка: {response.status}, {await response.text()}")
                return None

    # print("Полный ответ:", full_response)
    return full_response


# Заголовки для запросов к API Hugging Face
headers = {"Authorization": f"Bearer {TOKEN_TRANSFORMRS_API}"}

# Функция для отправки аудио в API Whisper через Hugging Face
def query_wisper(data):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    response = requests.post(
        API_URL,
        headers=headers,
        data=data
    )
    # print(response.status_code)
    result = response.json().get('text')
    # print(result)  # Можно убрать после отладки
    return result


# Хэндлер для команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    description = (
        "👋 **Добро пожаловать в интеллектуального помощника RUTUBE!**\n\n"
        "Наш видеохостинг ежедневно получает тысячи запросов от пользователей, касающихся различных аспектов работы платформы. "
        "Сегодня каждый запрос обрабатывается вручную операторами службы поддержки, что требует значительных временных и финансовых ресурсов.\n\n"
        "Мы предлагаем инновационное решение: **интеллектуальный помощник**, который автоматизирует ответы на часто задаваемые вопросы, "
        "используя нашу обширную базу знаний. Этот бот не только ускоряет процесс обработки запросов, но и повышает точность ответов, "
        "позволяя пользователям получать помощь быстрее и эффективнее.\n\n"
        "🔹 **Преимущества**:\n"
        "- Быстрая обработка текстовых запросов\n"
        "- Возможность отправки голосовых сообщений, которые бот распознает и преобразует в текст\n"
        "- Точные и релевантные ответы на основе базы знаний\n"
        "- Интеграция с Telegram для удобного взаимодействия\n\n"
        "📲 **Как это работает**:\n"
        "- Вы можете отправить текстовое сообщение с вопросом — бот моментально ответит на него, используя свою базу знаний.\n"
        "- Также можно отправить голосовое сообщение, и бот преобразует речь в текст, а затем ответит так же быстро и точно, как на текстовый запрос.\n\n"
        "Начните работу прямо сейчас — задайте свой вопрос, будь то текстовое или голосовое сообщение, и получите мгновенный ответ!"
    )

    await message.answer(description, parse_mode='Markdown')


# Хэндлер для обработки голосовых сообщений
@dp.message(F.voice)
async def handle_voice_message(message: Message):
    # Получаем файл голосового сообщения через bot.get_file()
    voice_file_info = await bot.get_file(message.voice.file_id)
    
    # Скачиваем голосовое сообщение
    file_path = f"voice_{message.message_id}.ogg"
    await bot.download_file(voice_file_info.file_path, destination=file_path)

    # Конвертируем ogg в wav для отправки в API Whisper
    sound = AudioSegment.from_ogg(file_path)
    wav_path = f"voice_{message.message_id}.wav"
    sound.export(wav_path, format="wav")

    # Открываем файл и отправляем его в API
    with open(wav_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    try:
        # Распознаем текст через API Whisper
        query = query_wisper(audio_data)

        if query:
            await message.answer(f"📢 Распознал ваш запрос: *{query}*", parse_mode="Markdown")

            # Передаем распознанный текст в функцию обработки запроса
            await process_text_query(message, query)
        else:
            await message.answer("🛑 Извините, не удалось распознать голосовое сообщение.")
    
    except Exception as e:
        await message.answer(f"⚠ Ошибка при обращении к сервису распознавания: {e}")

    # Удаляем временные файлы
    os.remove(file_path)
    os.remove(wav_path)


# Хранилище для отслеживания состояния диалога (в реальных условиях можно использовать базу данных)
user_states = {}
user_questions = {}  # Словарь для хранения исходных вопросов

# Функция для обработки текстовых запросов (например, введенного текста или распознанного голосом сообщения)
async def process_text_query(message: Message, query: str):
    # Поиск наиболее релевантного заголовка и ответа
    best_match_title, best_match_content = find_best_match(query)
    # print(best_match_content)
    classes = await sync_to_async(QueryAnswer.objects.filter(answer=best_match_content).first)()
    # return Response({'answer': best_match_content, 'class_1':classes.class_1, 'class_2':classes.class_2})

    if best_match_content:
        best_match_content = (
            f"**Ответ из БЗ:** `{best_match_content}`\n"
            f"**Классификатор 1 уровня:** `{classes.class_1}`\n"
            f"**Классификатор 2 уровня:** `{classes.class_2}`\n"
        )
        # Список шаблонов для быстрого ответа с пояснением
        quick_response_templates = [
            "💡 *Быстрый ответ, который может помочь*:\n\n{content}",
            "🔍 *Вот предварительный ответ на ваш запрос*:\n\n{content}",
            "📋 *Вот, что я нашел в базе знаний*:\n\n{content}",
            "🤔 *Первичный ответ на ваш вопрос*:\n\n{content}",
        ]

        # Формируем быстрый ответ с использованием случайного шаблона
        quick_response = random.choice(quick_response_templates).format(content=best_match_content)

        # Отправляем быстрый ответ пользователю
        await message.answer(quick_response, parse_mode="Markdown")
        
        try:
            # Генерация более детализированного ответа на основе запроса
            detailed_response = await generate_detailed_response(query, best_match_content, best_match_title)
        except ClientConnectorError:
            detailed_response = "LLAMA 3 не доступна или не была загружена! Попробуйте позднее."

        # Список шаблонов для детализированного ответа с пояснением
        detailed_response_templates = [
            "💡 *Вот более развернутый ответ для вас*:\n\n{response}",
            "🔍 *Детализированный ответ, содержащий больше информации*:\n\n{response}",
            "📋 *Подробный ответ на ваш вопрос*:\n\n{response}",
            "📝 *Дополнительные сведения по вашему запросу*:\n\n{response}",
        ]

        # Формируем детализированный ответ с использованием случайного шаблона
        detailed_response_text = random.choice(detailed_response_templates).format(response=detailed_response)

        # Отправляем детализированный ответ пользователю
        await message.answer(detailed_response_text, parse_mode="Markdown")

        # Спросим, удовлетворил ли ответ пользователя
        await message.answer("Вас устроил ответ?", reply_markup=yes_no_keyboard())
        
        # Сохраним состояние пользователя для последующего отслеживания
        user_states[message.from_user.id] = "waiting_feedback"
        user_questions[message.from_user.id] = query  # Сохраняем вопрос

    else:
        # Сообщение об отсутствии ответа
        no_answer = "😔 К сожалению, я не нашел ответ на ваш запрос. Попробуйте задать вопрос по-другому."
        await message.answer(no_answer)


# Функция для записи отклоненного вопроса в базу данных
async def save_question_for_operator(user_id: int, question: str):
    # Логика для записи в базу данных
    # Например, можно сохранить данные в SQL, MongoDB или другой системе
    print(f"Вопрос от пользователя с ID {user_id} сохранён для обработки оператором: '{question}'")

    # Пример записи в логи (или это может быть реальная база данных)
    # with db_connection.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT INTO rejected_questions (user_id, question, status) VALUES (%s, %s, %s)",
    #         (user_id, question, "pending")
    #     )
    # db_connection.commit()


# Определяем состояние формы обратной связи
class FeedbackForm(StatesGroup):
    waiting_for_contact_info = State()

# Состояния пользователей для отслеживания этапов
user_states = {}

# Обработка оценки ответа специалистом ("Да" или "Нет")
@dp.message(lambda message: message.text in ["Да", "Нет"])
async def handle_feedback(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # Проверяем, если пользователь в состоянии ожидания обратной связи
    if user_states.get(user_id) == "waiting_feedback":
        if message.text == "Да":
            # Специалист согласился, что ответ верный. Отправляем его пользователю
            await message.answer("✅ Спасибо! Ответ подтверждён и отправлен пользователю.")
            
            # Здесь можно добавить логику для отправки ответа конечному пользователю
            # Например, отправить уведомление или сообщение пользователю
            
            # Сбрасываем состояние
            user_states[user_id] = None
            await state.clear()
            await message.answer("🔄 Как еще могу помочь вам?", reply_markup=types.ReplyKeyboardRemove())

        # elif message.text == "Нет":
        #     # Специалист считает, что ответ неверный, предлагаем доработку
        #     await message.answer("⚠️ Ответ признан неверным. Какую информацию нужно исправить?")
            
        #     # Переводим пользователя в состояние ожидания указания на ошибки
        #     await state.set_state(FeedbackForm.waiting_for_contact_info)
        elif message.text == "Нет":
            # Специалист считает, что ответ неверный, выводим исходный вопрос пользователя
            question = user_questions.get(user_id, "Вопрос не найден.")
            await message.answer(f"⚠️ Ответ признан неверным. Вот исходный вопрос, на который нужно ответить заново: '{question}'")

            # Сохраняем вопрос в базу данных для дальнейшей обработки оператором
            await save_question_for_operator(user_id, question)
            await message.answer("❗ Вопрос отправлен на доработку оператору.")

            # Логика для сброса состояния после отклонения
            user_states[user_id] = None
            await state.clear()


# # Обработка ввода информации о неверном ответе
# @dp.message(FeedbackForm.waiting_for_contact_info)
# async def process_incorrect_info(message: types.Message, state: FSMContext):
#     incorrect_info = message.text

#     # Логика для отправки запроса на доработку (например, специалист может описать проблему)
#     await message.answer(f"❗ Спасибо! Информация о доработке передана: '{incorrect_info}'. Мы пересмотрим ответ.")

#     # Здесь можно добавить логику уведомления команды о необходимости доработки ответа
    
#     # Сбрасываем состояние после того, как специалист ввел нужную информацию
#     await state.clear()
#     await message.answer("🔄 Как еще могу помочь вам?", reply_markup=types.ReplyKeyboardRemove())


# Клавиатура для специалиста, чтобы выбрать правильность ответа
def yes_no_keyboard():
    keyboard = [
        [types.KeyboardButton(text="Да")],
        [types.KeyboardButton(text="Нет")]
    ]
    return types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


# Хэндлер для текстовых сообщений
@dp.message(F.text)
async def handle_message(message: Message):
    query = message.text
    await process_text_query(message, query)


# Запуск бота
async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
