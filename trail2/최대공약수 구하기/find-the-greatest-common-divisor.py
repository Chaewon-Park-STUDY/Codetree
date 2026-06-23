n, m = map(int, input().split())

# Please write your code here.

def max(n,m):
    arr=[]
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            arr.append(i)
    print(arr[len(arr)-1])

max(n,m)