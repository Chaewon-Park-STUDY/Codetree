n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(1,n):
    grid[0][i]=max(grid[0][i],grid[0][i-1])
    grid[i][0]=max(grid[i][0],grid[i-1][0])

for i in range(1,n):
    for j in range(1,n):
        grid[i][j]=min(max(grid[i][j],grid[i-1][j]),max(grid[i][j],grid[i][j-1]))



print(grid[n-1][n-1])