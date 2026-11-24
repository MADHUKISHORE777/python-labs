weight = int(input())
height = float(input())

if weight <= 0 or height <= 0:
    print("Invalid Input")
else:
    bmi = weight / (height * height)

    print("BMI =", bmi)

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Slightly overweight")
    elif bmi < 35:
        print("Obese")
    else:
        print("Clinically obese")