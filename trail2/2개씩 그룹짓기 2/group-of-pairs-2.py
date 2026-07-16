n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

store=[]

for i in range(n):
    store.append(arr[i+n]-arr[i])
print(min(store))