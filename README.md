[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
# Телеграм-бот
Телеграм-бот, который обрщается к API сервиса Практикум.Домашка. 
Узнаёт, взята ли ваша домашка в ревью, проверена, есть ли ошибки или принята. 
Отправляет результат в ваш Телеграм-чат.
## Установка:
1. Клонируйте репозиторий на локальную машину.
- ``git clone https://github.com/da-semenov/api_sp1_bot``
2. Установите виртуальное окружение.
- ``python3 -m venv venv``
3. Активируйте виртуальное окружение.
- ``source venv/bin/activate``
4. Установите зависимости.
- ``pip install -r requirements.txt``
5. Заполнить токены и chat_id (_PRACTICUM_TOKEN_, _TELEGRAM_TOKEN_, _TELEGRAM_CHAT_ID_)
- `` .env``
6. Запустите локальный сервер.
- ``python3 manage.py runserver``
 
## Основные использованные технологии
* [python 3.8](https://www.python.org/)
* [django](https://www.djangoproject.com/)

## Автор
* **Семенов Денис** - [da-semenov](https://github.com/da-semenov)
