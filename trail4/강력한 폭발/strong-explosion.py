n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[1,0,-1,0],[0,1,0,-1]


#폭탄리스트
store=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            store.append((i,j))

m=len(store)

result=[] #모든 순서쌍 집합
arr=[]

def apply(arr):
    result.append(tuple(arr))


def candid(num,x,y):
    if num==1:
        store=[(x-2,y),(x-1,y),(x,y),(x+1,y),(x+2,y)]
        for elem in store:
            nx,ny=elem[0],elem[1]
            if in_range(nx,ny):
                possible[nx][ny]="X"
    elif num==2:
        store=[(x,y),(x-1,y),(x,y-1),(x,y+1),(x+1,y)]
        for elem in store:
            nx,ny=elem[0],elem[1]
            if in_range(nx,ny):
                possible[nx][ny]="X"
    else:
        store=[(x,y),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
        for elem in store:
            nx,ny=elem[0],elem[1]
            if in_range(nx,ny):
                possible[nx][ny]="X"

def count_num(possible):
    num=0
    for elem in possible:
        for _ in elem:
            if _=="X":
                num+=1
    return num

  
def choose(m):
    if len(arr)==m:
        return apply(arr)
    for i in range(1,4):
        arr.append(i)
        choose(m)
        arr.pop()

choose(m)


import copy

max_val=0
for i in range(len(result)):
    possible=copy.deepcopy(grid)
    for j in range(m):
        x,y=store[j][0],store[j][1]
        choice=result[i][j]
        candid(choice,x,y)
    count_num(possible)
    max_val=max(max_val,count_num(possible))


print(max_val)
