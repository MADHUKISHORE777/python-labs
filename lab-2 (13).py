basic = float(input())

if basic < 0:
    print("Invalid Input")
else:
    hra = basic * 20 / 100
    ta = basic * 5 / 100
    da = basic * 10 / 100

    gross = basic + hra + ta + da

    if gross < 300000:
        tax = 0
    elif gross <= 1000000:
        tax = gross * 10 / 100
    elif gross <= 2500000:
        tax = gross * 20 / 100
    else:
        tax = gross * 30 / 100

    print("Gross Salary =", gross)
    print("Income Tax =", tax)
    print("Salary after tax =", gross - tax)