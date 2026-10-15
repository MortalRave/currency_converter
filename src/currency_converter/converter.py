import requests

class CurrencyConverter:
    def __init__(self):
        # USD, EUR, GBP, HUF, CZK
        self._rates = {
            'USD': 3.93, 
            'EUR': 4.38,
            'GBP': 5.19,
            'HUF': 0.012,
            'CZK': 0.18}

        self.update_rates()

    def get_rate(self, currency):
        return self._rates.get(currency, None)

    def update_rates(self):
        try:
            print("Pobieram aktualne kursy walut z NBP...")
            url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"
            response = requests.get(url)
            data = response.json()

            rates_table = data[0]['rates']
            for rate in rates_table:
                currency = rate['code']
                if currency in self._rates:
                    self._rates[currency] = rate['mid']

            print("Pobrano aktualne kursy walut z NBP.")
            pass
        except Exception as e:
            print(f"Nie udało się pobrać kursów, używam zapisanych. Powód błędu: {e}")

    def convert(self, amount, target_currency):
        rate = self.get_rate(target_currency)
        if rate is None:
            raise ValueError(f"Currency {target_currency} not supported.")
        return round(amount / rate, 2)

calculator = CurrencyConverter()
print(calculator.convert(250,'EUR'))
