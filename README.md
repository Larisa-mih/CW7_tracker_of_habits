# CW7_tracker_of_habits

## Description
Этот проект представляет собой API-сервер для сервиса отслеживания полезных привычек. Проект предоставляет конечные точки для создания, 
изменения, просмотра и удаления полезных привычек, приятных привычек и пользователей. Проект предусматривает отправку 
сообщения через Telegram-бот.

## Installation
```
Вам нужно клонировать этот проект из Github:
```
git clone https://github.com/Larisa-mih/CW7_tracker_of_habits
```
Затем установить необходимые библиотеки и фреймворки. 
Выполните команду:
pip install -r requirements.txt
```
Когда все будет сделано на стороне компьютера, вам следует подключить базу данных.

## Environment variables
Для работы Трекера привычек необходимо создать файл «.env» с информацией о вашей почтовой службе и др. 
Пример этого файла вы можете увидеть в «.env.example».
Для работы отправки сообщений в Telegram вам понадобится Токен Telegram Bot.
```
# PostgreSql
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=


# Telegram
TOKEN_BOT=

REDIS_URL=
```

## Database connection
Вам нужно установить PosgreSQL. 
```
https://www.postgresql.org/download/
```

Затем создать Database.
```
CREATE DATABASE name_database;
```

Создать и применить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Celery
Для правильной работы Celery вам нужен Redis. После загрузки Redis вам следует его запустить командой```
celery -A config beat -l info
```

## Creating a superuser
Для создания суперюзера используйте команду
```
python manage.py csu
```

## Add test habits
Для тестирования используйте команду
```
coverage run --source='.' manage.py test
```
coverage report
```

## Documentation
Всю документацию по эндпоинтам вы можете посмотреть по ссылке
```
http://localhost:8000/docs/
http://localhost:8000/redoc/

## Deploy

Для развертывания проекта после клонирования и создания файла .env вам необходимо установить docker и docker-compose.
Затем вы можете использовать команды
```
docker-compose build
docker-compose up
```

или
```
docker-compose up -d —build
```

- перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Contacts

Ссылка на репозиторий: [https://github.com/Larisa-mih](https://github.com/Larisa-mih)