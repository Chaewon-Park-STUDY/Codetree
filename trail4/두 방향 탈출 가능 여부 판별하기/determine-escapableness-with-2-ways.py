n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs,dys=[1,0],[0,1]
dir=0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m


def two_way(x,y):
    if in_range(x,y+1) and grid[x][y+1]==1 and in_range(x+1,y) and grid[x+1][y]==1:
        return True

visited=[]
store=set()
back=0
if grid[0][0]==0:
    print(0)
else:
    x,y=0,0
    is_continue=True
    while is_continue:
        if x==n-1 and y==m-1:
            is_continue=False
            print(1)
            break
        nx,ny=x+dxs[dir],y+dys[dir]
        if two_way(x,y):
            if (x,y) not in store:
                visited.append((x,y,dir))
                store.add((x,y))

        if in_range(nx,ny) and grid[nx][ny]==1:
            x,y=x+dxs[dir],y+dys[dir]
        else:

            dir=(dir+1)%2
            nx,ny=x+dxs[dir],y+dys[dir]
            if in_range(nx,ny) and grid[nx][ny]==1:
                x,y=x+dxs[dir],y+dys[dir]
            elif in_range(nx,ny) and grid[nx][ny]==0:
                back+=1
                if len(visited)>0:
                    x, y, old_dir = visited.pop()
                    dir = (old_dir + 1) % 2
                else:
                    is_continue=False
                    print(0)
                    break
