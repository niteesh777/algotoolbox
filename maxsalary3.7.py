
a=int(input())
l=input().split()
l1=list()
for i in range(0,a):
    k=int(l[i])
    if(k<=9):
        l1.append(k)
    else:    
         while(k>9):
             k1=k%10
             k=k-k1
             k=k/10
             l1.append(k1)
         l1.append(int(k))
                  
l1.sort(reverse=True)

n=0
for i in range(0,len(l1)):
    n=n*10+l1[i]
print(n)    
        
