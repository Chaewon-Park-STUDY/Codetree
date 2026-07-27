n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

store=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==adjacent[0]:
            store.append((i,j))


for elem in store[::-1]:
    arr=[]
    x=elem[0]
    arr.append(x)
    for i in range(n-1):
        k= adjacent[i]-x
        if k not in arr and 1<=k<=n:
            arr.append(k)
            x=k
    if len(arr)==n:
        for elem in arr:
            print(elem, end=" ")
        break
