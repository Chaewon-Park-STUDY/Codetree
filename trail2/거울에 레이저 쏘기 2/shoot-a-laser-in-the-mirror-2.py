n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
# print("\\") 이렇게 해야지 \하나가 출력됨

for i in range(n):
    for j in range(n):
        if grid[i][j]=="/":
            grid[i][j]=1
        else:
            grid[i][j]=2

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[1,0,-1,0],[0,-1,0,1]

def direction(start):
    if 0<=start-1<n:
        dir=0
    elif n<=start-1<2*n:
        dir=1
    elif 2*n<=start-1<3*n:
        dir=2
    else:
        dir=3
    return dir

def detect_1(dir):
    if dir%2==0:
        dir+=1
    else:
        dir-=1
    return dir

def detect_2(dir):
    direction=3-dir
    return direction


is_continue=True
num=0
if 0<=k-1<n:
    dir=direction(k)
    x,y=-1,k-1
elif n<=k-1<2*n:
    dir=direction(k)
    x,y=k-1-n,n
elif 2*n<=k-1<3*n:
    dir=direction(k)
    x,y=n,3*n-k
else:
    dir=direction(k)
    x,y=4*n-k,-1
while is_continue:
    nx,ny=x+dxs[dir],y+dys[dir]
    if in_range(nx,ny)==False:
        is_continue=False
        break
    else:
        num+=1
        if grid[nx][ny]==1:
            x,y=x+dxs[dir],y+dys[dir]
            dir=detect_1(dir)
        else:
            x,y=x+dxs[dir],y+dys[dir]
            dir=detect_2(dir)

print(num)

