n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


num=0
for elem in grid:
    for i in range(n-m+1):
        store=[]
        for _ in elem[i:i+m]:
            if _ not in store:
                store.append(_)
        if len(store)==1:
            num+=1
            break

for i in range(n):
    store=[]
    for j in range(n):
        store.append(grid[j][i])
    for k in range(n-m+1):
        new=[]
        for _ in store[k:k+m]:
            if _ not in new:
                new.append(_)
        if len(new)==1:
            num+=1
            break
print(num)