n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def game_over(arr):
    num=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=="X":
                num+=1
    if num==n**2:
        return True

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
dxs,dys=[-1,1,0,0],[0,0,-1,1]

def move(x,y):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and grid[nx][ny]==1 and possible[nx][ny]!="X":
            return nx,ny
    return False


def candid(x,y):
    num=0
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and grid[nx][ny]==1 and possible[nx][ny]!="X":
            num+=1
            arr.append((nx,ny))
    if num>=2:
        return arr
    return False


possible=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]==0:
            possible[i][j]="X"
is_continue=True
store=[]
while is_continue:
    if game_over(possible):
        is_continue=False
        break
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1 and possible[i][j]!="X":
                x,y=i,j
                num=1
                possible[x][y]="X"
                stack=[]
                while True:
                    if move(x,y)!=False:
                        if candid(x,y)==False:
                            x,y=move(x,y)
                            possible[x][y]="X"
                            num+=1
                        else:
                            possible[x][y]="X"
                            arr=candid(x,y)
                            for elem in arr:
                                stack.append(elem)

                            x,y=stack.pop()
                            possible[x][y]="X"
                            num+=1
                    else:

                        if len(stack)>0:
                            x,y=stack.pop()
                            if possible[x][y]!="X":
                                possible[x][y]="X"
                                num+=1
                        else:
                            possible[x][y]="X"
                            store.append(num)
                            break

print(len(store))
store.sort()
for elem in store:
    print(elem)