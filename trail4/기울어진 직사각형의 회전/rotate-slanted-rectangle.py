n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

r-=1
c-=1

dxs,dys=[-1,-1,1,1],[1,-1,-1,1]
x,y,=r,c
is_continue=True
start=0
store=[]
store.append(grid[x][y])


def rotate(dir,x,y):
    x,y=x+dxs[dir],y+dys[dir]
    return x,y,grid[x][y]

while is_continue:
    if start<m1:
        x,y,value=rotate(0,x,y)
        store.append(value)
    elif m1<=start<m1+m2:
        x,y,value=rotate(1,x,y)
        store.append(value)
    elif m1+m2<=start<m1+m2+m3:
        x,y,value=rotate(2,x,y)
        store.append(value)
    elif start<=m1+m2+m3+m4-2:
        x,y,value=rotate(3,x,y)
        store.append(value)
    start+=1

    if start==m1+m2+m3+m4-1:
        is_continue=False
        start=0

x,y=r,c
arr=[]
if dir==0:
    while True:
        if start<m1:
            x,y,value=rotate(0,x,y)
            grid[x][y]=store[start]
        elif m1<=start<m1+m2:
            x,y,value=rotate(1,x,y)
            grid[x][y]=store[start]
        elif m1+m2<=start<m1+m2+m3:
            x,y,value=rotate(2,x,y)
            grid[x][y]=store[start]
        elif start<=m1+m2+m3+m4-1:
            x,y,value=rotate(3,x,y)
            grid[x][y]=store[start]
        start+=1

        if start==m1+m2+m3+m4:
            break
else:
    for elem in store[2:]:
        arr.append(elem)
    arr.append(store[0])
    arr.append(store[1])
    while True:
        if start<m1:
            x,y,value=rotate(0,x,y)
            grid[x][y]=arr[start]
        elif m1<=start<m1+m2:
            x,y,value=rotate(1,x,y)
            grid[x][y]=arr[start]
        elif m1+m2<=start<m1+m2+m3:
            x,y,value=rotate(2,x,y)
            grid[x][y]=arr[start]
        elif start<=m1+m2+m3+m4-1:
            x,y,value=rotate(3,x,y)
            grid[x][y]=arr[start]
        start+=1

        if start==m1+m2+m3+m4:
            break








for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()
    
    