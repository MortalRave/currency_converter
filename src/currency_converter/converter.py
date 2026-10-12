class CurrencyConverter:
    def __init__(self):
        # USD, EUR, GBP, HUF, CZK
        self.rates = {
            'USD': 3.93, 
            'EUR': 4.38,
            'GBP': 5.19,
            'HUF': 0.012,
            'CZK': 0.18}

    def convert(self, amount, target_currency):
        return amount / self.rates[target_currency]

calculator = CurrencyConverter()
print(calculator.convert(250,'EUR'))
