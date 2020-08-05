def fibo(a):
    f=[0,1]
    for i in range(2,a+1):
        f.append((f[i-1]+f[i-2])%10)
    return(f[a]%10)    

    
 
a=input().split(" ")
a1=int(a[0])
a2=int(a[1])
sum=((fibo(a2+2)-1)-(fibo(a1+2)-1))+fibo(a1)
print(sum%10)
    


    

    
