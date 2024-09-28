from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from sentence_transformers import SentenceTransformer
from chat_bot.models import QueryAnswer
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize



# Создание эмбеддингов для заголовков и контента
print("Создаём и нормализуем эмбендинги")
faq_data = QueryAnswer.objects.all()
faq_data_dict = {item.query: item.answer for item in faq_data}
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "models")
os.makedirs(model_path, exist_ok=True)
# Инициализация модели эмбеддингов
# model = SentenceTransformer('BAAI/bge-m3')
# model.save(model_path)
model = SentenceTransformer(model_path)

# Создание эмбеддингов для заголовков и контента
titles = [item.query for item in faq_data]
# contents = [item.answer for item in faq_data]

title_embeddings = model.encode(titles)
# content_embeddings = model.encode(contents)
print("Готов к работе!")


class GenerateAnswerModelView(APIView):
    def post(self, request):
        user_query = request.data['question']
        # Преобразование запроса пользователя в эмбеддинг
        user_query_embedding = model.encode([user_query])
        similarity_threshold = 0.6  # Пороговое значение для сходства

        # Поиск наиболее релевантного заголовка
        title_similarity_scores = cosine_similarity(user_query_embedding, title_embeddings)
        best_title_idx = title_similarity_scores.argmax()
        if title_similarity_scores[0][best_title_idx] < similarity_threshold:
            return Response({'answer': "Не могу ответить", 'class_1': 'None', 'class_2': 'None'})
        

        # Поиск наиболее релевантного контента
        # content_similarity_scores = cosine_similarity(user_query_embedding, content_embeddings)
        # best_content_idx = content_similarity_scores.argmax()

        # Получение заголовка и контента
        best_match_title = titles[best_title_idx]
        # best_match_content = contents[best_content_idx]
        best_match_content = faq_data_dict.get(best_match_title, None)
        # if best_match_content is None:
        #     best_match_content = contents[best_content_idx]
        classes = QueryAnswer.objects.filter(answer=best_match_content).first()
        return Response({'answer': best_match_content, 'class_1':classes.class_1, 'class_2':classes.class_2})
        # Генерация ответа через Gradio
        #response = generate_gradio_answer(best_match_title, best_match_content, user_query)
