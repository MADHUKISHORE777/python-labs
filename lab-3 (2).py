x1=float(input("x1:"))
y1=float(input("y1:"))
r=(x1**2 + y1**2)**1/2
print(r)
x2=float(input("x2:"))
y2=float(input("y2:"))
d=((x2-x1)**2+(y2-y1)**2)**1/2
print(d)
if  d>r:
    print("inside the boundary")
elif  d<r:
    print("outside the boundary")
else:
    print("on the boundary")
    