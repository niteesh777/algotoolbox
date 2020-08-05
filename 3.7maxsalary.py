def compar(e):
    if(e>9):
        while(e>9):
            e1=e%10
            e=e-e1
            e=e/10
        return e
    else:
        return(e)
def comp2(d,md):
    return (int(str(d)+str(md))>=int(str(md)+str(d)))

def ln(l1):
    n=list()
    while(l1!=[]):
        md=0
        for d in l1:
            if comp2(d,md):
                md=d
        n.append(md)
        l1.remove(md)
    return(n)

a=int(input())
l=input().split()
l1=list()
for i in range(0,a):
    l1.append(int(l[i]))
    
            
print(l1)



    
    
    
