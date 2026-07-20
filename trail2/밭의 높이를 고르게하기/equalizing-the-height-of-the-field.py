N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

store=[]

for i in range(N):
    if arr[i]<H:
        store.append(H-arr[i])
    else:
        store.append(arr[i]-H)

min_value= 100000
for i in range(N-T+1):
    num=0
    for j in range(i,i+T):
        num+=store[j]
    min_value= min(min_value,num)

print(min_value)