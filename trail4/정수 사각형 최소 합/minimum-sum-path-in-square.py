n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


for i in range(n-2,-1,-1):
    grid[0][i]=grid[0][i]+grid[0][i+1]

for i in range(1,n):
    grid[i][n-1]=grid[i][n-1]+grid[i-1][n-1]

for i in range(1,n):
    for j in range(n-2,-1,-1):
        grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j+1])
print(grid[n-1][0])