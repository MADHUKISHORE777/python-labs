n = int(input())
if n <= 0:
    print("Invalid number")

else:
    for i in range(1, 21):
        print(n, "x", i, "=", n * i)