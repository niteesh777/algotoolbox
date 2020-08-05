d=int(input())
mx=int(input())
st=int(input())
ar=input().split()
ar1=list()
ar1.append(0)
for i in range(0,st):
    ar1.append(int(ar[i]))
ar1.append(d)    

c=0
n=0
while(c<=st):
    l=c
    while(c<=st and (ar1[c+1]-ar1[l])<=mx):
        c=c+1
    if(c==l):
        n=-1
        break
    if(c<=st):
        n=n+1
   
print(n)            
