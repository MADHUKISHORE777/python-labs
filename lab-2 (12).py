a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print("Largest =", a)
    else:
        print("Largest =", c)
else:
    if b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)