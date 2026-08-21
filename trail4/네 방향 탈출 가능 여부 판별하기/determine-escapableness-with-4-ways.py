n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

dxs,dys=[1,0,-1,0],[0,1,0,-1]
possible=[[0 for _ in range(m)]for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            possible[i][j]="X"

def candid(x,y):
    num=0
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and a[nx][ny]==1:
            num+=1
            arr.append((nx,ny))
    if num>=2:
        return arr
    return False

def move(x,y):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and a[nx][ny]==1:
            return nx,ny
    return False

x,y=0,-1
is_continue=True
stack=[]
success=0
while is_continue:
    if x==n-1 and y==m-1:
        is_continue=False
        success=1
        break
    if candid(x,y)==False:
        if move(x,y)!=False:
            x,y=move(x,y)
            possible[x][y]="X"
        else:
            if stack:
                x,y=stack.pop()
                if possible[x][y]!="X":
                    possible[x][y]="X"
            else:
                is_continue=False
                break
    else:
        stack.extend(candid(x,y))
        x,y=stack.pop()
        if possible[x][y]!="X":
            possible[x][y]="X"


                        

print(success)