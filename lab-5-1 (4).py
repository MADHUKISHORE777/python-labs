n = int(input())
fact = 1

if n < 0:
    print("Invalid input")
else:
    while n > 0:
        fact *= n
        n -= 1

    print(fact)