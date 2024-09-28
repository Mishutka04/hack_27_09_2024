FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
ADD . /backend/

# Устанавливаем зависимости
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN pip install --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

EXPOSE 8000


