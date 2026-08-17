n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.

start=[[1,6],[2,5],[3,4]]

def in_range(x,y):
    return 1<=x and x<=n and 1<=y and y<=n
dxs,dys=[0,0,-1,1],[-1,1,0,0]
def direction(dir):
    if dir=="L":
        return 0
    elif dir=="R":
        return 1
    elif dir=="U":
        return 2
    else:
        return 3

def convert(dir,new):
    if dir%2==0:
        new[0].reverse()
        if dir==0:
            new[0],new[2]=new[2],new[0]
        else:
            new[0],new[1]=new[1],new[0]
    else:
        if dir==1:
            new[2].reverse()
            new[0],new[2]=new[2],new[0]
        else:
            new[1].reverse()
            new[0],new[1]=new[1],new[0]
    return new

x,y=r,c
grid=[
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

grid[x][y]=6
new=start.copy()
for i in range(m):
    dir=direction(directions[i])
    nx,ny=x+dxs[dir],y+dys[dir]
    if in_range(nx,ny):
        x,y=x+dxs[dir],y+dys[dir]
        new=convert(dir,new)
        grid[x][y]=new[0][1]
sum_val=0
for elem in grid:
    for _ in elem:
        sum_val+=_
print(sum_val)
        
