n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

possible=[[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[1,0,-1,0],[0,1,0,-1]

def candid(x,y,start_x,start_y):
    num=0
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and grid[nx][ny]==grid[start_x][start_y]:
            num+=1
            arr.append((nx,ny))
    if num>=2:
        return arr
    return False

def move(x,y,start_x,start_y):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and possible[nx][ny]!="X" and grid[nx][ny]==grid[start_x][start_y]:
            return nx,ny
    return False

store=[]
for i in range(n):
    for j in range(n):
        if possible[i][j]!="X":
            is_continue=True
            x,y=i,j
            start_x,start_y=i,j
            possible[x][y]="X"
            stack=[]
            num=1
            while is_continue:
                if candid(x,y,start_x,start_y)==False:
                    if move(x,y,start_x,start_y)==False:
                        if stack:
                            x,y=stack.pop()
                            if possible[x][y]!="X":
                                possible[x][y]="X"
                                num+=1
                        else:
                            is_continue=False
                            store.append(num)
                            break
                     
                    else:
                        x,y=move(x,y,start_x,start_y)
                        possible[x][y]="X"
                        num+=1

                else:
                    stack.extend(candid(x,y,start_x,start_y))
                    x,y=stack.pop()
                    if possible[x][y]!="X":
                        possible[x][y]="X"
                        num+=1
                    
sum_val=0
for elem in store:
    if elem>=4:
        sum_val+=1

print(sum_val,max(store))