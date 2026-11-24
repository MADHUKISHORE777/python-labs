
radius = float(input("Enter radius (1-100): "))

if 1 <= radius <= 100:
    area = 2.15 * radius * radius
    print("Area of circle =", area)
else:
    print("Invalid Input")