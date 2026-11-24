cost = int(input())
revenue = int(input())

if revenue == cost:
    print("Break even")
elif revenue > cost:
    print("Profit =", revenue - cost)
else:
    print("Loss =", cost - revenue)