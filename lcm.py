import math
a=input().split()
a1=int(a[0])
a2=int(a[1])
g=math.gcd(a1,a2)
print(int((a1*a2)/g))
