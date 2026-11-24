x = int(input())
y = int(input())

if x <= 0 or y <= 0:
    print("Invalid Input")
elif y % x == 0:
    print("y is divisible by x")
else:
    print("y is not divisible by x")