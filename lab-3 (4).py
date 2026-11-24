a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))

if a <= 0 or b <= 0 or c <= 0 :
    print("invalid:")
else:
    print("these angles form triange")
     
if a<90 and b<90 and c<90:
    print("angle form acute angled triangle")
elif a==90 or b==90 or c==90:
    print("angles form right angled triangle")
else:
    print("form obtuse angled triangle")
    
     
     