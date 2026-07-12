N = int(input())
seat = input()

# Please write your code here.
seat=list(seat)

arr=[0 for _ in range(N+1)]

for i in range(1,N+1):
    arr[i]=int(seat[i-1])

store=[]

min_val=100

for i in range(1,N+1):
    if arr[i]==1:
        for j in range(i+1,N+1):
            if arr[j]==1:
                min_val= min(min_val, j-i)
new=min_val

for j in range(1,N+1):
    new=min_val
    if arr[j]!=1:
        for k in range(1,N+1):
            if arr[k]==1:
                new= min(new, abs(j-k))
        store.append(new)
print(max(store))
    