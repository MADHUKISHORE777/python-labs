b = float(input())
s = input()
if b <= 100:
    p = "Bulgaria"
    if s == "summer":
        c = b * 0.3
    else:
        c = b * 0.7

elif b <= 1000:
    p = "Balkans"
    if s == "summer":
        c = b * 0.4
    else:
        c = b * 0.8

else:
    p = "Europe"
    c = b * 0.9

if s == "summer" and p != "Europe":
    stay = "Camp"
else:
    stay = "Hotel"

print(p)
print(stay)
print("Money spent:", c)
