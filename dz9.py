import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        response = requests.get(
            "https://bank.gov.ua/ua/markets/exchangerates/"
        )
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all(
            "td", {"data-label": "Офіційний курс"}
        )
        res = soup_list[8] #dollar - 8 element
        self.rate = float(res.text.replace(",", "."))
    def convert(self, uah):
        return uah / self.rate


converter = CurrencyConverter()
uah = float(input("Введіть суму в гривнях: "))
usd = converter.convert(uah)
print(f"Сума в доларах США: {usd:.2f} USD")