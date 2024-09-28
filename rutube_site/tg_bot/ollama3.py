import aiohttp
import asyncio
import json

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

    print("Полный ответ:", full_response)
    return full_response

# Пример вызова
async def main():
    query = "Что такое искусственный интеллект?"
    best_match_content = "Искусственный интеллект - это..."
    best_match_title = "Искусственный интеллект"
    
    result = await generate_detailed_response(query, best_match_content, best_match_title)
    print(result)

# Запуск основного асинхронного кода
asyncio.run(main())
