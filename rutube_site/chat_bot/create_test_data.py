import random
import json
import pandas as pd
import os

# Пример словаря с 800 вопросами и ответами
base_dir = os.path.dirname(os.path.abspath(__file__))
faq_users = pd.read_excel(os.path.join(base_dir, "02.xlsx"))
faq_users_dict = {
    row['Вопрос пользователя']: {
        'Ответ из БЗ': row['Ответ из БЗ'],
        'Классификатор 1 уровня': row['Классификатор 1 уровня'],
        'Классификатор 2 уровня': row['Классификатор 2 уровня']
    }
    for _, row in faq_users.iterrows()
}

# Количество случайных вопросов, которые нужно выбрать
num_questions = 50

# Случайным образом выбираем 50 вопросов
random_questions = random.sample(list(faq_users_dict.keys()), num_questions)

# Формируем список данных для тестирования
test_data = []
for question in random_questions:
    test_data.append({
        "question": question,
        "answer": faq_users_dict[question]["Ответ из БЗ"],
        "class_1": faq_users_dict[question]["Классификатор 1 уровня"],
        "class_2": faq_users_dict[question]["Классификатор 2 уровня"]
    })

# Сохраняем результат в файл test_data.json
with open(os.path.join(base_dir, 'test_data.json'), 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=4)

print(f"{num_questions} вопросов сохранены в test_data.json")
