ar1=input().split()
s=int(ar1[0])
n=int(ar1[1])
a=list()
for i in range (0,s):
    ar2=input().split()
    b=list()
    b.append(int(ar2[0]))
    b.append(int(ar2[1]))
    a.append(b)
ar3=input().split()
c=list()
for i in range(0,n):
    c.append(int(ar3[i]))

f=list()
for i in range(0,n):
    v=0
    for j in range(0,s):
        if(a[j][0]<=c[i] and c[i]<=a[j][1]):
            v=v+1
    f.append(v)
for i in range(0,n):
    print(f[i],end=" ")
    
            
    
