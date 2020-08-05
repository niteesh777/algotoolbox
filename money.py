import math
a=int(input())
b=0
c=0
if(a>=10):
    b=math.floor(a/10)
    a=a%10
if(a>=5):
    c=math.(a/5)
    a=a-5
if(a>=1):
    a=a
print(a+b+c)    
    
