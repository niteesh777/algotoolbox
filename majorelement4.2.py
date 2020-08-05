a=int(input())
b=input().split()
arr=list()
for i in range(0,a):
    arr.append(int(b[i]))
arr.sort()
v=0
c=0
for i in range(0,a):
    if(i==0):
        k=arr[0]
        c=c+1
    else:
        if(k==arr[i]):
            c=c+1
            
        else:
            k=arr[i]
            c=1
            
    if(c > a/2):
        v=v+1
        break
if(v>=1):
    print(1)
else:
    print(0)

        
    
    
