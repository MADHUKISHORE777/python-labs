income = float(input())

if income < 0:
    print("Invalid Income")

elif income <= 20000:
    tax = 0.02 * income
    print("Tax =", tax)

elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
    print("Tax =", tax)

else:
    tax = 1150 + 0.035 * (income - 50000)
    print("Tax =", tax)