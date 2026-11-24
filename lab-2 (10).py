n = int(input())

if n < 0:
    print("Invalid Input")
elif n >= 100:
    cost = n * 0.20
    print("Total cost = $", cost)
else:
    cost = n * 0.25
    print("Total cost = $", cost)