n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

max_val=0
def adding(arr):
    global max_val
    num=0
    if m>1:
        num=arr[0]^arr[1]
        for i in range(2,m):
            num=num^arr[i]
        max_val=max(max_val,num)
    else:
        num=arr[0]
        max_val=max(max_val,arr[0])

arr=[]

start=0
def choose(n,m,start):
    if len(arr)==m:
        return adding(arr)
    
    for i in range(start,n):
        arr.append(A[i])
        start=i
        choose(n,m,start+1)
        arr.pop()
choose(n,m,start)


print(max_val)




