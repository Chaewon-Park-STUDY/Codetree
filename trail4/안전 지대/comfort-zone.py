n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
min_val=100
max_val=0
for elem in grid:
    max_val=max(max_val,max(elem))
    min_val=min(min_val,min(elem))

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
dxs,dys=[1,0,-1,0],[0,1,0,-1]

def move(x,y,arr):
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and arr[nx][ny]!="X":
            return nx,ny

    return False

def candid(x,y,arr):
    num=0
    store=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and arr[nx][ny]!="X":
            num+=1
            store.append((nx,ny))
    if num>=2:
        return store
    else:
        return False

final={}
for k in range(min_val,max_val):
    store=[]
    possible=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]<=k:
                possible[i][j]="X"
    for i in range(n):
        for j in range(m):
            is_continue=True
            if possible[i][j]!="X":
                num=1
                x,y=i,j
                possible[x][y]="X"
                stack=[]
                while is_continue:
                    if move(x,y,possible)!=False:
                        if candid(x,y,possible)==False:
                            x,y=move(x,y,possible)
                            num+=1
                            possible[x][y]="X"
                        else:
                            stack.extend(candid(x,y,possible))
                            x,y=stack.pop()
                            if possible[x][y]!="X":
                                possible[x][y]="X"
                                num+=1
                    else:
                        if stack:
                            x,y=stack.pop()
                            if possible[x][y]!="X":
                                possible[x][y]="X"
                                num+=1
                        else:
                            store.append(num)
                            is_continue=False
                            break
                

    final[k]=len(store)

answer=0
val_k=0
for pos in final:
    answer=max(answer,final.get(pos))
for pos in final:
    if final.get(pos)==answer:
        val_k=pos
        break
if min_val!=max_val:
    print(val_k, answer, end=" ")
else:
    if min_val==1:
        print(1,0)
    else:
        print(min_val-1,n*m)
