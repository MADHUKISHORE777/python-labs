months = int(input())

if months < 0:
    print("Invalid Input")
else:
    years = months // 12
    remaining = months % 12

    print("Years =", years)
    print("Months =", remaining)