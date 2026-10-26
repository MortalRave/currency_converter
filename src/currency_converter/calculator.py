class Calculator:
    def calculate(self, expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            return "ERROR"