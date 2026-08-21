n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

possible=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            possible[i][j]="X"

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[1,0,-1,0],[0,1,0,-1]

def candid(x,y):
    num=0
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and grid[nx][ny]==0:
            num+=1
            arr.append((nx,ny))
    if num>=2:
        return arr
    return False

def move(x,y):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and grid[nx][ny]==0:
            return nx,ny
    return False


num=0
stack=[]
for i in range(k):
    is_continue=True
    x,y=points[i][0]-1,points[i][1]-1
    if possible[x][y]!="X":
        possible[x][y]="X"
        num+=1
    while is_continue:
        if candid(x,y)==False:
            if move(x,y)==False:
                if stack:
                    x,y=stack.pop()
                    if possible[x][y]!="X":
                        possible[x][y]="X"
                        num+=1
                else:
                    is_continue=False
                    break
            else:
                x,y=move(x,y)
                possible[x][y]="X"
                num+=1
        else:
            stack.extend(candid(x,y))
            x,y=stack.pop()
            if possible[x][y]!="X":
                possible[x][y]="X"
                num+=1
print(num)