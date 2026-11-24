s = input()
i = 0
cap = small = digit = special = 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        cap += 1
    elif 'a' <= s[i] <= 'z':
        small += 1
    elif '0' <= s[i] <= '9':
        digit += 1
    else:
        special += 1

    i += 1

print("Capital:", cap)
print("Small:", small)
print("Digits:", digit)
print("Special:", special)