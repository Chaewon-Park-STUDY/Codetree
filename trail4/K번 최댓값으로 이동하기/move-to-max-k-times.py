n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r-=1
c-=1

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[-1,0,1,0],[0,1,0,-1]

def candid(x,y):
    num=0
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X":
            num+=1
            arr.append((nx,ny))
    if num>=2:
        return arr
    return False

def move(x,y):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X":
            return nx,ny
    return False




x,y=r,c
for m in range(k):
    is_continue=True
    possible=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]>=grid[x][y]:
                possible[i][j]="X"
    store=[]
    stack=[]
    start_x,start_y=x,y
    while is_continue:
        if candid(x,y)==False:
            if move(x,y)==False:
                if stack:
                    x,y=stack.pop()
                    if possible[x][y]!="X":
                        possible[x][y]="X"
                        if grid[x][y] not in store:
                            store.append(grid[x][y])
                else:
                    is_continue=False
                    break
            else:
                x,y=move(x,y)
                possible[x][y]="X"
                if grid[x][y] not in store:
                    store.append(grid[x][y])
        else:
            stack.extend(candid(x,y))
            x,y=stack.pop()
            if possible[x][y]!="X":
                possible[x][y]="X"
                if grid[x][y] not in store:
                    store.append(grid[x][y])
    if x==start_x and y==start_y:
        break
    cnt={}
    a=max(store)
    cnt[a]=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==a and possible[i][j]=="X":
                cnt.get(a).append((i,j))
    x,y=cnt.get(a)[0][0],cnt.get(a)[0][1]
print(x+1,y+1)