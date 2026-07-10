n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
x_cor=[p[0]-1 for p in points]
y_cor=[p[1]-1 for p in points]

dir_num=0
dxs,dys=[0,1,0,-1],[1,0,-1,0]   #동 남 서 북 

grid=[
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

for i in range(m):
    grid[x_cor[i]][y_cor[i]]=1
    cnt=0
    for j in range(4):
        nx,ny=x_cor[i]+dxs[dir_num], y_cor[i]+dys[dir_num]
        if in_range(nx,ny) and grid[nx][ny]==1:
            cnt+=1
        dir_num= (dir_num+1)%4
    if cnt==3:
        print(1)
    else:
        print(0)
