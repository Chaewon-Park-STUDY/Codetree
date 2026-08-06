n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
# grid[r-1][c-1]-1의 값만큼 상하좌우만틈

interval=grid[r-1][c-1]-1

x,y=r-1,c-1
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

for i in range(r-2,r-2-interval,-1):
    if in_range(i,c-1):
        grid[i][c-1]=0
for i in range(r,r+interval):
    if in_range(i,c-1):
        grid[i][c-1]=0
for j in range(c-2,c-2-interval,-1):
    if in_range(r-1,j):
        grid[r-1][j]=0
for j in range(c,c+interval):
    if in_range(r-1,j):
        grid[r-1][j]=0

grid[r-1][c-1]=0



for i in range(n): #열
    for j in range(n-1,-1,-1):
        num=0
        for k in range(j+1,n):
            if grid[k][i]==0:
                num+=1
        if num>0:
            grid[j+num][i]=grid[j][i]
            grid[j][i]=0

for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()