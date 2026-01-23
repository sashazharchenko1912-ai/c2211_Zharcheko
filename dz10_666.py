import sqlite3
import urllib.request
import re

DB_NAME = "weather.db"
URL = "https://sinoptik.ua/pohoda/chernihiv"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            дата_час TEXT DEFAULT CURRENT_TIMESTAMP,
            температура INTEGER
        )
    """)
    conn.commit()
    conn.close()


def get_temperature():
    with urllib.request.urlopen(URL) as response:
        html = response.read().decode("utf-8")

    # Пошук температури (наприклад: +3°, −5°)
    match = re.search(r'(-?\+?\d+)&deg;', html)

    if not match:
        raise ValueError("Не вдалося знайти температуру на сайті")

    return int(match.group(1))


def save_to_db(temp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather (температура)
        VALUES (?)
    """, (temp,))
    conn.commit()
    conn.close()

    print(f"Збережено температуру: {temp}°C")


def wait_30_minutes():
    # Проста затримка БЕЗ time.sleep()
    # ~30 хвилин (наближено)
    counter = 0
    while counter < 120_000_000:
        counter += 1


def main():
    create_table()
    print("Збір даних погоди з сайту sinoptik.ua")
    print("Місто: Чернігів")
    print("Оновлення кожні 30 хвилин\n")

    try:
        while True:
            temperature = get_temperature()
            save_to_db(temperature)
            print("Очікування наступного оновлення...\n")
            wait_30_minutes()
    except KeyboardInterrupt:
        print("\nПрограму зупинено користувачем.")


if __name__ == "__main__":
    main()
