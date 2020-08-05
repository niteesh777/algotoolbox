import math
def bsearch(a,low,high,key):
    if(low>high):
         return -1
    else:
        k=math.floor((high-low)/2)
        mid=(low+k)
        if(a[mid]==key):
            return mid
        elif(a[mid]>key):
            return bsearch(a,low,mid-1,key)
        else:
            return bsearch(a,mid+1,high,key)

ar1=input().split()
ar2=input().split()
a=list()
an=list()
for i in range(1,int(ar1[0])+1):
    a.append(int(ar1[i]))
a.sort()
for i in range(1,int(ar2[0])+1):
    k=bsearch(a,0,len(a)-1,int(ar2[i]))
    an.append(k)
for i in range(0,len(an)):
    print(an[i],end=" ")
               
               
    

    
