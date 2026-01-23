import requests


class CurrencyConverter:
    def __init__(self, base_currency="UAH", target_currency="USD"):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = self._get_usd_rate()

    def _get_usd_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
        params = {
            "valcode": "USD",
            "json": ""
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data[0]["rate"]

    def convert_to_usd(self, amount):
        return amount / self.rate


def main():
    converter = CurrencyConverter()

    print("Офіційний курс долара США (НБУ):")
    print(f"1 USD = {converter.rate:.2f} UAH\n")

    try:
        amount = float(input("Введіть суму в гривнях (UAH): "))
        result = converter.convert_to_usd(amount)
        print(f"\n{amount:.2f} UAH = {result:.2f} USD")
    except ValueError:
        print("Помилка: введіть коректне числове значення.")


if __name__ == "__main__":
    main()
