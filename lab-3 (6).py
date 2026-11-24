x=int(input())

if x<10000 or x>99999:
    print("invaild")
else:
    a1 = x // 10000
    a2 = (x//1000)%10
    a3 = (x//100)%10
    a4 = (x//10)%10
    a5 = x%10
    
    lar=a1
    pos=1

    if a2>lar:
        lar=a2
        pos=2
    if a3>lar:
        lar=a3
        pos=3
    if a4>lar:
        lar=a4
        pos=4
    if a5>lar:
        lar=a5
        pos=5
    print("largest digit:",lar)
    print("position from left:",pos)