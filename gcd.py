a=input().split(" ")
b=int(a[0])
c=int(a[1])
if(b<c):
    (b,c)=(c,b)

r=b%c
while(r!=0):
    b=c
    c=r
    r=b%c


print(c)    

    
    
    
