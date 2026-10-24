from flask import Flask, render_template, request
from src.currency_converter.converter import CurrencyConverter
from src.currency_converter.bmi import BMICalculator
from src.currency_converter.calculator import Calculator

app = Flask(__name__)

converter = CurrencyConverter()
bmi_calc = BMICalculator()
calc = Calculator()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/currency', methods=['GET', 'POST'])
def currency():
    result = None
    target_currency = None
    currency_rate = None

    if request.method == 'POST':
        amount = float(request.form['amount'])
        target_currency = request.form['currency']
        result = converter.convert(amount, target_currency)
        currency_rate = converter.get_rate(target_currency)

    return render_template('converter.html', 
                           result=result, 
                           target_currency=target_currency,
                           currency_rate=currency_rate
                           )

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi = None
    weight = None
    height = None
    status = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi,status = bmi_calc.calculate(weight, height)
        

    return render_template('bmi.html',
                            result=bmi,
                            status=status)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        result = calc.calculate(expression)
        print(f"Równanie: {expression} | Wynik: {result}")

    return render_template('calculator.html',
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)