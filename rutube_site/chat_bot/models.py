from django.db import models

class QueryAnswer(models.Model):
    """
    Модель для хранения запросов и ответов.
    Хранит текстовые поля для запроса (query) и ответа (answer).
    """

    query = models.TextField(verbose_name="Запрос")
    answer = models.TextField(verbose_name="Ответ")
    class_1 = models.TextField(verbose_name="Класс 1")
    class_2 = models.TextField(verbose_name="Класс 2")

    class Meta:
        verbose_name = "Ответ на запрос"
        verbose_name_plural = "Ответы на запросы"
        ordering = ['-id']  # Последние добавленные записи отображаются первыми

    def __str__(self):
        """
        Возвращает строковое представление модели, отображая первые 50 символов запроса.
        """
        return f"Запрос: {self.query[:50]}..."

    def get_summary(self):
        """
        Метод для получения краткого представления ответа.
        Возвращает первые 100 символов ответа.
        """
        return f"{self.answer[:100]}..."
