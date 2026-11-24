V = int(input())
N = int(input())

if V < 0 or N < 0:
    print("Invalid input")

else:
    if N == 0:
        print("Water quantity =", V)
    elif N == 1:
        V = V * 0.95 + 10
        print("Water quantity =", V)
    elif N == 2:
        V = (V * 0.95 + 10) * 0.95 + 10
        print("Water quantity =", V)
    elif N == 3:
        