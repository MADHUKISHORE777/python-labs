n = int(input())
a = b = 0

while True:
    x = int(input())

    if x == -999:
        break

    if x % n == 0:
        a += 1
    else:
        b += 1

print("Divisible:", a)
print("Not divisible:", b)