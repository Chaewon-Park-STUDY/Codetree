n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
num=0
for p in range(1,n):
    if all(grid[p][j]==0 for j in range(k-1,k+m-1)):
        num+=1
        if num==n-1:
            for j in range(k-1,k+m-1):
                grid[n-1][j]=1
        else:
            continue
    else:
        for j in range(k-1,k+m-1):
            grid[p-1][j]=1
        break
   
if n==1 and grid.count([0])==1:
    print(1)
else:
    for elem in grid:
            for _ in elem:
                print(_, end=" ")
            print()