def fibo(a):
    f=[0,1]
    for i in range(2,a+1):
        f.append((f[i-1]+f[i-2])%10)
    return(f[a]%10)    

    
 
a=int(input())
pro=fibo(a)*fibo(a+1)
print(pro%10)
    

    
