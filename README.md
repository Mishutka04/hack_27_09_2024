<h1>Интеллектуальный помощник оператора службы поддержки RUTUBE</h1>

<p align='center'><img width=100% src='https://www.iguides.ru/upload/medialibrary/7a3/9v3avq2t6ddk9r2u42y9zuf0obtl9oc0.png' /></p>

<h2>Цели проекта</h2>

<p align='justify'>Видеохостинг RUTUBE ежедневно сталкивается с тысячами пользовательских обращений, связанных с различными аспектами использования сервиса. В настоящее время каждое из таких обращений обрабатывается вручную операторами службы поддержки, что приводит к значительным временным и денежным затратам.</p>
<p align='justify'>Цель состоит в разработке системы интеллектуального помощника для генерации ответов на основе базы знаний часто задаваемых вопросов и целевых ответов на них. Система должна демонстрировать высокую точность и скорость работы, а также быть интегрирована с Telegram ботом для улучшения пользовательского взаимодействия.</p>

<h2>Решение</h2>

<h3>Интеллектуальный Помощник RUTUBE Telegram BOT: Высокая Точность и Интуитивное Взаимодействие</h3>

<p align='justify'>Интеллектуальный помощник RUTUBE, построенный на моделях BERT BAAI/bge-m3 и LLAMA 3, обеспечивает мгновенные и точные ответы, превращая взаимодействие в удобный и эффективный процесс. Он способен обрабатывать как текстовые, так и голосовые запросы, автоматически распознавая речь и преобразуя её в текст для дальнейшего анализа.
</p>

<h3>Преимущества помощника RUTUBE:</h3>

<p align='justify'>Высокая точность и релевантность ответов благодаря глубокому пониманию смысла запросов.</p>

<h3>Поддержка голосовых сообщений:</h3>

<p align='justify'>Помощник легко распознаёт аудиосообщения и отвечает так же оперативно, как и на текстовые запросы.
Интеграция с платформой RUTUBE позволяет пользователям получать быстрые ответы на вопросы о контенте, функциях и возможностях сервиса.
Интуитивный интерфейс и мгновенная обработка запросов обеспечивают плавное и комфортное взаимодействие, делая помощника RUTUBE идеальным инструментом для улучшения пользовательского опыта и поддержки аудитории платформы.</p>

<h3>Backend на Django для Интеллектуального Помощника RUTUBE: Преимущества и Архитектурные Решения</h3>
<p align='justify'>Django обеспечивает высокую производительность и надёжность при разработке серверной части интеллектуального помощника RUTUBE. Этот фреймворк предоставляет мощные инструменты для реализации REST API, что делает интеграцию с фронтендом быстрой и простой. Поддержка современных архитектурных паттернов и асинхронных возможностей позволяет легко масштабировать проект и обрабатывать большое количество запросов параллельно.</p>

<p align='justify'>Использование модели BERT BAAI/bge-m3 для обработки запросов обеспечивает глубокий анализ текста и релевантные ответы. Django ORM упрощает работу с базой данных, а встроенные механизмы безопасности защищают приложение от возможных уязвимостей. REST API предоставляет удобный способ обмена данными, обеспечивая быстрый доступ к функционалу бота из любой среды.</p>

<p align='justify'>Пользователи получают точные и оперативные ответы, будь то текстовые или голосовые запросы. Архитектура на Django делает взаимодействие с сервисом интуитивным и надёжным, поддерживая стабильную производительность и качественное обслуживание.</p>

<h3>Front-end для чат-бота на React: Преимущества и Пользовательский Опыт</h3>

<p align='justify'>React обеспечивает компонентный подход, который облегчает поддержку и расширение кода, а также высокую производительность благодаря виртуальному DOM. Одностраничное приложение позволяет быстро взаимодействовать без перезагрузок страницы, а интеграция с API упрощает получение и отображение данных от чат-бота. React также предлагает гибкость в дизайне, поддерживая адаптивную вёрстку и различные CSS-фреймворки.</p>

<p align='justify'>Пользователи получают интуитивный интерфейс, где взаимодействие с ботом происходит моментально. Приложение адаптируется под любые устройства, обеспечивая удобство и быстрые ответы, что улучшает общее впечатление от использования.</p>

## Экономическая эффективность решения
## Принцип работы API 
<p align='center'><img src='https://grozny.tv/storage/images/ec61c7af-3ba7-44e7-adb0-6a1f23d84edd.jpg' width='100%' /></p>
<h2>Перенос проекта на локальную машину</h2>
<p>Для переноса проекта на локалькую машину необходимо склонировать проект с этого GitHub репозитория</p>

```sh
    git init
    git clone https://github.com/Mishutka04/hack_27_09_2024.git
```

<h2>Сборка и запуск проекта на Docker</h2>
<p>Для запуска проетка на Docker он <b>должен</b> быть установлен на вашей локальной машине!</p>
<h3>Для запуска и сборки на операционной системе Windows</h3>

```sh
    docker-compose build
```

```sh
    docker-compose up
```

<hr />
<h3>Для запуска и сборки на операционной Linux-подобной системе</h3>

```sh
    sudo docker-compose up --build
```

<h3>Если сборка проекта не требуется</h3>

```sh
    docker-compose up
```
<hr />

<h3>Для запуска и работы Телеграм бота</h3>

```sh
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    docker exec -it ollama ollama run llama3:8b
```

<h3>Работа с Back-end сервисом</h3>  
<p>Если сборка и запуск проекта на Docker вам не подходит, то мы предлагаем вручную скомпилировать и запустить проект</p>

```sh
    Доделать
```

<h3>Работа с Front-end сервисом</h3>
<p>Для запуска сайта необходимо перейти в необходимую папку с проектом</p>

```sh
    cd front-end
```

<p>Установить зависимости пакетов</p>

```sh
    npm i
    npm i react-responsive
```

<p>Запустить проект в разработку</p>

```sh
    npm run dev
```

<p>После этого Vite автоматически сгенирирует сервер на локальной машине. Нажатием по ссылке с зажатым ctrl вы автоматически перейдете в браузер с запущеным сайтом</p>

![image](https://github.com/user-attachments/assets/6c525898-5c99-4385-aa43-5b4003f8c40b)
