salary = float(input())
years = int(input())
if years > 5:
    bonus = salary * 5 / 100
else:
    bonus = 0
print("Net bonus amount:", bonus)