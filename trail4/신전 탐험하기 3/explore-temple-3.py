n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

grid=a.copy()

for i in range(1,n):
    for j in range(m):
        a=0
        for k in range(m):
            if k!=j:
                a=max(a,grid[i-1][k])
        grid[i][j]+=a

print(max(grid[n-1]))
                