Проект блога 
================
## Проект позволяет делать посты, комментировать их и подписываться на автора.

#### В проекте используется Python 3, Django 2.2, Django Rest Framework и SQL.

## Как запустить проект:

###### Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/dimkafaint/api_yamdb

cd yatube

###### Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

###### Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

###### Выполнить миграции:

cd yatube

python3 manage.py migrate

###### Запустить проект:

python3 manage.py runserver

###### Автор:
- Храповицкий Дмитрий https://github.com/dimkafaint
