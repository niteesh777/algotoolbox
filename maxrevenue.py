a=int(input())
if(a==1):
    b=int(input())
    c=int(input())
    print(b*c)
else:
    b=input().split()
    c=input().split()
    b1=list()
    c1=list()
    for i in range(0,a):
        b1.append(int(b[i]))
        c1.append(int(c[i]))
    b1.sort()
    c1.sort()
    sum=0
    for i in range(0,a):
        sum=sum+(b1[i]*c1[i])
    print(sum)    
