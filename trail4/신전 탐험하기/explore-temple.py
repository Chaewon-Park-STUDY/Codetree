n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

grid=[[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    grid[i][0]=l[i]
    grid[i][1]=m[i]
    grid[i][2]=r[i]

for i in range(1,n):
    grid[i][0]+=max(grid[i-1][1],grid[i-1][2])
    grid[i][1]+=max(grid[i-1][0],grid[i-1][2])
    grid[i][2]+=max(grid[i-1][0],grid[i-1][1])
print(max(grid[n-1]))

