x=int(input("enter 3 digit number:"))

if x<100 or x>999:
    print("invaild")
else:
    d1=x//100
    d2=(x//10)%10
    d3=x%10
    
    digit_sum=d1+d2+d3
    
if x%digit_sum==0:
    print(x,"is harshad number")
else:
    print(x,"is not harshad number")
    