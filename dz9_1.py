import requests
from datetime import datetime


class CurrencyConverter:
    def __init__(self, base_currency: str = "UAH", target_currency: str = "USD"):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = self._get_usd_rate()

    def _get_usd_rate(self) -> float:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
        params = {
            "valcode": "USD",
            "json": ""
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data[0]["rate"]

    def convert_to_usd(self, amount: float) -> float:
        return amount / self.rate


def main():
    converter = CurrencyConverter()

    print(f"Офіційний курс НБУ станом на {datetime.now().date()}:")
    print(f"1 USD = {converter.rate:.2f} UAH\n")

    try:
        amount = float(input("Введіть суму в гривнях (UAH): "))
        result = converter.convert_to_usd(amount)
        print(f"\n{amount:.2f} UAH = {result:.2f} USD")
    except ValueError:
        print("Помилка: введіть коректне числове значення.")


if __name__ == "__main__":
    main()
