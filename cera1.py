a=int(input())
b=input().split(" ")
c=list()
for i in range(0,a):
    c.append(int(b[i]))

c.sort(reverse=True)
print(c[0]*c[1])
             
             
    
