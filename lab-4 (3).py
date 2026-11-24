print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

choice = int(input())

if choice == 1:
    side = int(input())
    area = side * side

elif choice == 2:
    length = int(input())
    breadth = int(input())
    area = length * breadth

elif choice == 3:
    radius = int(input())
    area = 2.15 * radius * radius

elif choice == 4:
    base = int(input( ))
    height = int(input())
    area = 0.5 * base * height

else:
    area = -1

if area >= 0:
    print("Area:", round(area, 3))
else:
    print("Invalid choice")