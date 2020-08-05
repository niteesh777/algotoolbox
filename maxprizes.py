a=int(input())
t=0
l=list()
i=0
while(a!=0):
    i=i+1
    if((a-i)!=0):
        if(i==1):
            l.append(i)
            a=a-i
            t=t+1
        elif(l[i-2]<(a)):
            l.append(i)
            a=a-i
            t=t+1
        else:
            l[i-2]=a+(i-1)
            a=0
    else:
        l.append(a)
        a=0
        t=t+1
print(t)
for i in range(0,len(l)):
    print(l[i],end=" ")

            
            
       
            
    
    
    

