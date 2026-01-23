import sqlite3
import requests
from datetime import datetime
import time

CITY = "Kyiv"
DB_NAME = "weather.db"
UPDATE_TIME = 1800  # 30 минут

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            datetime TEXT NOT NULL,
            temperature TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_temperature():
    url = f"https://wttr.in/{CITY}?format=3"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Пример ответа: "Kyiv: +18°C"
    text = response.text.strip()

    if ":" not in text:
        raise ValueError("Неверный формат ответа")

    return text.split(":", 1)[1].strip()

def save_to_db(temp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather (datetime, temperature) VALUES (?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp)
    )
    conn.commit()
    conn.close()

def main():
    create_db()
    print("Программа запущена. Ctrl+C — остановка.")

    while True:
        try:
            temp = get_temperature()
            save_to_db(temp)
            print(f"{datetime.now()} | Температура: {temp}")
        except Exception as e:
            print("Ошибка:", e)

        time.sleep(UPDATE_TIME)

main()
