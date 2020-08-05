a=int(input())
b=input().split()
arr=list()
for i in range(0,a):
    arr.append(int(b[i]))
arr.sort()
for i in range(0,len(arr)):
    print(arr[i],end=" ")
