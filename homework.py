import logging
import os
import time

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()


PRACTICUM_TOKEN = os.getenv("PRACTICUM_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_TOKEN)
url = "https://praktikum.yandex.ru/api/user_api/homework_statuses/"

logging.basicConfig(
    filename="homework.log",
    format="%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s",
)


def parse_homework_status(homework):
    homework_name = homework["homework_name"]
    if homework["status"] == "approved":
        verdict = (
            "Ревьюеру всё понравилось, можно приступать к следующему уроку."
        )
    elif homework["status"] == "rejected":
        verdict = "К сожалению в работе нашлись ошибки."
    else:
        logging.error("Похоже изменился формат статусов.")
        return "Ошибка статуса."
    return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'


def get_homework_statuses(current_timestamp):
    if current_timestamp is None:
        logging.error("Ошибка:Что-то с форматом данных")
        raise Exception("Ошибка формата данных")
    headers = {"Authorization": f"OAuth {PRACTICUM_TOKEN}"}
    data = {
        "from_date": current_timestamp
    }
    try:
        homework_statuses = requests.get(url=url, params=data, headers=headers)
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка запроса к серверу: {e}")
    return homework_statuses.json()


def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)


def main():
    current_timestamp = int(time.time())  # начальное значение timestamp

    while True:
        try:
            new_homework = get_homework_statuses(current_timestamp)
            if new_homework.get("homeworks"):
                send_message(
                    parse_homework_status(new_homework.get("homeworks")[0])
                )
            current_timestamp = new_homework.get(
                "current_date"
            )  # обновить timestamp
            time.sleep(60 * 20)  # опрашивать раз в 20 минут

        except Exception as e:
            logging.error(f"Бот упал с ошибкой: {e}")
            time.sleep(60 * 20)
            continue


if __name__ == "__main__":
    main()
