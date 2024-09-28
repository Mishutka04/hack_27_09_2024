import requests
import json
from difflib import SequenceMatcher

# Функция для сравнения строк с использованием SequenceMatcher
def compare_strings(expected, actual):
    return SequenceMatcher(None, expected, actual).ratio()

# Функция для вычисления точности ответов
def calculate_accuracy(expected_answer, actual_answer, expected_class_1, actual_class_1, expected_class_2, actual_class_2):
    answer_accuracy = compare_strings(expected_answer, actual_answer)
    class_1_accuracy = compare_strings(expected_class_1, actual_class_1)
    class_2_accuracy = compare_strings(expected_class_2, actual_class_2)

    return answer_accuracy, class_1_accuracy, class_2_accuracy

# URL конечной точки API
# api_url = "http://127.0.0.1:8000/api/model/"
api_url = "http://192.144.12.86:8000/api/model/"

# Загрузка эталонных данных из JSON файла
with open('./rutube_site/chat_bot/data.json', 'r', encoding='utf-8') as file:
    test_data = json.load(file)

# Для записи результатов тестирования
results = []

# Цикл для отправки запросов и получения ответов
for item in test_data:
    question = item['question']
    expected_answer = item['answer']
    expected_class_1 = item['class_1']
    expected_class_2 = item['class_2']

    # Формируем запрос
    request_data = {"question": question}
    
    try:
        # Отправляем POST-запрос на конечную точку API
        response = requests.post(api_url, json=request_data)
        
        # Проверка успешности запроса
        if response.status_code == 200:
            response_data = response.json()

            actual_answer = response_data.get('answer', "")
            actual_class_1 = response_data.get('class_1', "")
            actual_class_2 = response_data.get('class_2', "")

            # Вычисляем точность для ответа и классов
            answer_accuracy, class_1_accuracy, class_2_accuracy = calculate_accuracy(
                expected_answer, actual_answer, expected_class_1, actual_class_1, expected_class_2, actual_class_2
            )

            # Сохраняем результаты для каждого запроса
            results.append({
                "question": question,
                "expected_answer": expected_answer,
                "actual_answer": actual_answer,
                "answer_accuracy": answer_accuracy,
                "expected_class_1": expected_class_1,
                "actual_class_1": actual_class_1,
                "class_1_accuracy": class_1_accuracy,
                "expected_class_2": expected_class_2,
                "actual_class_2": actual_class_2,
                "class_2_accuracy": class_2_accuracy
            })

        else:
            # Если запрос не был успешным, сохраняем статус ошибки
            results.append({
                "question": question,
                "error": f"Ошибка запроса. Код: {response.status_code}, Сообщение: {response.text}"
            })
    
    except requests.exceptions.RequestException as e:
        # Если произошла ошибка сети
        results.append({
            "question": question,
            "error": f"Ошибка сети: {str(e)}"
        })

# Выводим результаты тестирования
for result in results:
    if "error" in result:
        print(f"❌ Ошибка для вопроса '{result['question']}': {result['error']}")
    else:
        print(f"🔍 Вопрос: {result['question']}")
        print(f"Ожидаемый ответ: {result['expected_answer']}")
        print(f"Фактический ответ: {result['actual_answer']}")
        print(f"Точность ответа: {result['answer_accuracy']:.2f}")
        print(f"Ожидаемый класс 1: {result['expected_class_1']} -> Фактический: {result['actual_class_1']} (Точность: {result['class_1_accuracy']:.2f})")
        print(f"Ожидаемый класс 2: {result['expected_class_2']} -> Фактический: {result['actual_class_2']} (Точность: {result['class_2_accuracy']:.2f})")
        print("")

# Суммируем общую точность по всем вопросам
total_accuracy = sum([r['answer_accuracy'] for r in results if "error" not in r]) / len([r for r in results if "error" not in r])
print(f"Общая точность ответов: {total_accuracy:.2f}")


# ssh user1@192.144.12.86
# qwerty12
# source venv/bin/activate
# python ./rutube_site/manage.py runserver 0.0.0.0:8000

# 1 - hack_27_09_msk/rutube_site/chat_bot/test_api.py нужно заменить api_url = "http://192.144.12.86:8000/api/model/"
# 2 - ну и  перефразировать "question"  в этом файле. hack_27_09_msk/rutube_site/chat_bot/test_data.json
# 3 - возможно подкорректировать ответы чатбота rutube_site/tg_bot/bot.py
# 4 - преза
# 5 - скринкаст
# 6 - если что то забыл допишите