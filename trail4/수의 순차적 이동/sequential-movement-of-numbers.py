n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs,dys=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

start=1
is_continue=True

while is_continue:
    num=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==start:
                num+=1
                store=[]
                x,y=i,j
                for k in range(8):
                    dir=k
                    nx,ny=x+dxs[dir],y+dys[dir]
                    if in_range(nx,ny):
                        store.append(grid[nx][ny])
                for k in range(8):
                    dir=k
                    nx,ny=x+dxs[dir],y+dys[dir]
                    if in_range(nx,ny) and grid[nx][ny]==max(store):
                        grid[i][j]=grid[nx][ny]
                        grid[nx][ny]=start
                break
        if num==1:
            break      

    start+=1
    if start==n*n+1:
        m-=1
        start=1
        if m==0:
            is_continue=False

for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()