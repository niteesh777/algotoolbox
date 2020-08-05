a=int(input())
b=0
c=1
for i in range(0,a-1):
    d=b+c
    b=c
    c=d
if(a!=0 and a!=1):
    print(d%10)
if(a==0):
    print(0)
if(a==1):
    print(1)
    
    
    
