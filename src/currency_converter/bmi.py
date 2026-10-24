class BMICalculator:
    # kg / cm 
    def calculate(self, weight, height):
        bmi = round(weight / (height / 100) ** 2, 2)
        stauts = ""
        if bmi < 18.5:
            status = "niedowaga"
        elif bmi >= 18.5 and bmi < 25:
            status = "prawidłowa masa ciała"
        elif bmi >= 25 and bmi < 30:
            status = "nadwaga"
        else:
            status = "otyłość"
        return bmi, status
    