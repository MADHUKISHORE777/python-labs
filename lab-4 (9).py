n = int(input())
total = 0
if n <= 0:
    print("Invalid input")

else:
    for i in range(n):
        num = int(input("Enter number: "))
        total = total + num

    print("Sum =", total)