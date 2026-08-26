n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.

store=[]

def collect(arr):
    store.append(arr.copy())


arr=[]

idx=[_ for _ in range(1,n**2+1)]
num=[0 for _ in range(n**2)]

count_num=0

while True:
    for i in range(n):
        for j in range(n):
            num[count_num]=(i,j)
            count_num+=1
            if count_num==n**2:
                break
            continue
        if count_num==n**2:
            break
        continue
    if count_num==n**2:
        break
        
start=0
def choose(n,m,start):
    if len(arr)==m:
        return collect(arr)

    for i in range(start,n**2):
        x,y=num[i][0],num[i][1]
        if grid[x][y]==1 and (x,y) not in arr:
            arr.append((x,y))
            start=i
            choose(n,m,start+1)
            arr.pop()


choose(n,m,start)

dxs,dys=[1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def move(x,y):
    candid=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and possible[nx][ny]!=1:
            candid.append((nx,ny))
    if len(candid)>0:
        return candid
    return False


def count_num(possible):
    num=0
    for elem in possible:
        for _ in elem:
            if _=="X":
                num+=1
    return num



import copy
max_val=0
for i in range(len(store)):
    possible=copy.deepcopy(grid)
    for elem in store[i]:
        x,y=elem[0],elem[1]
        possible[x][y]=0
    for p in range(k):
        stack=[]
        x,y=r[p],c[p]
        possible[x][y]="X"
        while True:
            if move(x,y)==False:
                if stack:
                    x,y=stack.pop()
                    if possible[x][y]!="X":
                        possible[x][y]="X"
                else:
                    break
            else:
                stack.extend(move(x,y))
                x,y=stack.pop()
                if possible[x][y]!="X":
                    possible[x][y]="X"
    max_val=max(max_val,count_num(possible))
print(max_val)

        
