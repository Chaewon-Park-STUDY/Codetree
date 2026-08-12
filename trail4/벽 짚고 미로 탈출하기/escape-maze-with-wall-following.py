N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.

def in_range(a,b):
    return 1<=a and a<N+1 and 1<=b and b<N+1

is_continue=True
dir=0
time=0
dxs,dys=[0,-1,0,1],[1,0,-1,0] #동북서남


def is_right(dir,x,y): #오른쪽에 벽이 있는지
    dir=(dir+3)%4
    nx,ny=x+dxs[dir],y+dys[dir]
    if in_range(nx,ny):
        if grid[nx][ny]=="#":
            return True

def block(dir,x,y): 
    nx,ny=x+dxs[dir],y+dys[dir]
    if in_range(nx,ny):
        if grid[nx][ny]=="#":
            return True

def out_of_grid(dir,x,y):
    nx,ny=x+dxs[dir],y+dys[dir]
    if is_right(dir,x,y) and not in_range(nx,ny) and not block(dir,x,y):
        return True
revisit=set()

while is_continue:
    if (x,y,dir) in revisit:
        time=-1
        is_continue=False
        break
    else:
        revisit.add((x,y,dir))

    if block(dir,x,y):
        dir=(dir+1)%4
        nx,ny=x+dxs[dir],y+dys[dir]
        if out_of_grid(dir,x,y):
            time+=1
            is_continue=False
            break
    else:
        if out_of_grid(dir,x,y):
            time+=1
            is_continue=False
            break
        else:
            nx,ny=x+dxs[dir],y+dys[dir]
            if is_right(dir,nx,ny) and in_range(nx,ny):
                x,y=x+dxs[dir],y+dys[dir]
                time+=1        
            else:
                nx,ny=x+dxs[dir],y+dys[dir]
                if in_range(nx,ny):
                    x,y=x+dxs[dir],y+dys[dir]
                    time+=1
                  
                  
                    dir=(dir+3)%4
                    nx,ny=x+dxs[dir],y+dys[dir]
                    if in_range(nx,ny):
                        time+=1
                        x,y,=x+dxs[dir],y+dys[dir]
                   

print(time)



        
