class Calculator:
    def calculate(self, expression):
        operation = expression.split(' ')

        if operation[1] == '+':
            return float(operation[0]) + float(operation[2])
        elif operation[1] == '-':
            return float(operation[0]) - float(operation[2])
        elif operation[1] == '*':
            return float(operation[0]) * float(operation[2])
        elif operation[1] == '/':
            if operation[2] == '0':
                return "ERROR: DZIELENIE ZERO"
            return float(operation[0]) / float(operation[2])
                
        