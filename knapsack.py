a=input().split()
t=list()
n=int(a[0])
m=int(a[1])
for i in range(0,n):
    l1=input().split(" ")
    li1=list()
    li1.append(int(l1[0]))
    li1.append(int(l1[1]))
    t.append(li1)
    
r=list()
p=0
for i in range(0,n):
    r.append(t[i][0]/t[i][1])
if(len(r)==1 and m>t[0][1] ):
        p=t[0][0]
else:
    while(m>0):
        v=max(r)
        i=r.index(v)
        r[i]=0
        if(m>=t[i][1]):
            m=m-t[i][1]
            p=p+t[i][0]
        elif(m<t[i][1]):
            k=t[i][1]/m
            m=0
            p=p+(t[i][0]/k)
print('%.3f'%p)        
    
    
    

        
    



           
