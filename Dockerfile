# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY ./rutube_app /app/backend
# COPY ./rutube_app/tg_bot /app/telegram_bot
COPY requirements.txt /app/

# Устанавливаем зависимости
#RUN apt-get -y update
#RUN apt-get -y upgrade
#RUN apt-get install -y ffmpeg
#RUN pip install --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt


# Открываем порт для Django
EXPOSE 8000

# Запускаем сервер Django и бота
CMD ["sh", "-c", "python /app/backend/manage.py makemigrations & python /app/backend/manage.py migrate & python /app/backend/manage.py runserver 0.0.0.0:8000 & python /app/backend/tg_bot/bot.py"]
