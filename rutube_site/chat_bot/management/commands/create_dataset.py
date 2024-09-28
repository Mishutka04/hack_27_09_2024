import os
import pandas as pd
from django.core.management.base import BaseCommand

from chat_bot.models import QueryAnswer


class Command(BaseCommand):
    help = 'Отображает текущее время'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        faq_bz = pd.read_excel(os.path.join(base_dir, "01.xlsx"))
        faq_bz_dict = {
            row['Вопрос из БЗ']: {
            'Ответ из БЗ': row['Ответ из БЗ'],
            'Классификатор 1 уровня': row['Классификатор 1 уровня'],
            'Классификатор 2 уровня': row['Классификатор 2 уровня']
                        }
            for _, row in faq_bz.iterrows()
        }

        faq_users = pd.read_excel(os.path.join(base_dir, "02.xlsx"))
        faq_users_dict = {
            row['Вопрос пользователя']: {
                'Ответ из БЗ': row['Ответ из БЗ'],
                'Классификатор 1 уровня': row['Классификатор 1 уровня'],
                'Классификатор 2 уровня': row['Классификатор 2 уровня']
                        }
                for _, row in faq_users.iterrows()
            }

        faq_data_dict = faq_bz_dict | faq_users_dict
        # Печать результата для проверки
        for section in faq_data_dict:
            QueryAnswer.objects.create(query=section, answer=faq_data_dict[section]['Ответ из БЗ'],
                                       class_1=faq_data_dict[section]['Классификатор 1 уровня'],class_2=faq_data_dict[section]['Классификатор 2 уровня'])
            print("Вопрос - ", section, "Ответ -", faq_data_dict[section]['Ответ из БЗ'],
                                       "Класс 1 - ", faq_data_dict[section]['Классификатор 1 уровня'], "Класс 2 - ", faq_data_dict[section]['Классификатор 2 уровня'])
        print("Finish")

