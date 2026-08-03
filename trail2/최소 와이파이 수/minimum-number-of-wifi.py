n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

num=0
wifi=[0 for _ in range(n)]
for i in range(m,n-m):
    if wifi[i-m]==0 and arr[i-m]==1:
        for j in range(i-m,i+m+1):
            wifi[j]=1
        num+=1

if any(wifi[k]==0 and arr[k]==1 for k in range(n)):
    num+=1
print(num)
