class CurrencyConverter:
    def __init__(self):
        # USD, EUR, GBP, HUF, CZK
        self._rates = {
            'USD': 3.93, 
            'EUR': 4.38,
            'GBP': 5.19,
            'HUF': 0.012,
            'CZK': 0.18}

    def get_rate(self, currency):
        return self._rates.get(currency, None)

    def convert(self, amount, target_currency):
        rate = self.get_rate(target_currency)
        if rate is None:
            raise ValueError(f"Currency {target_currency} not supported.")
        return round(amount / rate, 2)

calculator = CurrencyConverter()
print(calculator.convert(250,'EUR'))
