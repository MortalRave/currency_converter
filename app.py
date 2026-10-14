from flask import Flask, render_template, request
from src.currency_converter.converter import CurrencyConverter

app = Flask(__name__)

calculator = CurrencyConverter()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    target_currency = None
    currency_rate = None

    if request.method == 'POST':
        amount = float(request.form['amount'])
        target_currency = request.form['currency']
        result = calculator.convert(amount, target_currency)
        currency_rate = calculator.get_rate(target_currency)

    return render_template('index.html', 
                           result=result, 
                           target_currency=target_currency,
                           currency_rate=currency_rate
                           )

if __name__ == '__main__':
    app.run(debug=True)