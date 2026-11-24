x=int(input("enter four digited number"))

d1 = x //1000
d2 =(x //100) % 10
d3 =(x//10) % 10
d4 =x%10

sum_first_two=d1+d2
sum_last_two=d3+d4

print("sum of first two digits:",sum_first_two)
print("sum of last two digits:", sum_last_two)

if sum_first_two==sum_last_two:
    print("result: the two sums are equal")
else:
    print("result: the two sums are not equal")
    