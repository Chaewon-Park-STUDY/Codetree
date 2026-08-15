n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def direction(starting_point):
    if 0<=starting_point<n:
        dir=0
    elif n<=starting_point<2*n:
        dir=1
    elif 2*n<=starting_point<3*n:
        dir=2
    else:
        dir=3
    return dir


dxs,dys=[1,0,-1,0],[0,-1,0,1]


def detect_1(dir,nx,ny):
    if dir%2==0:
        dir+=1
    else:
        dir-=1
    return dir

def detect_2(dir,nx,ny):
    dir=3-dir
    return dir

def zero(nx,ny):
    if grid[nx][ny]==0:
        return True


max_val=0
cnt={}


for i in range(4*n):
    is_continue=True
    time=0
    store=[]
    visited=set()
    if 0<=i<n:
        x,y=-1,i
        dir=direction(i)
    elif n<=i<2*n:
        x,y=i-n,n
        dir=direction(i)
    elif 2*n<=i<3*n:
        x,y=n,3*n-1-i
        dir=direction(i)
    else:
        x,y=4*n-1-i,-1
        dir=direction(i)
    while is_continue:
            nx,ny=x+dxs[dir],y+dys[dir]
            if not in_range(nx,ny):
                time+=1
                max_val=max(max_val,time)
                is_continue=False
                break
            else:
                time+=1
                if zero(nx,ny)==True:
                    x,y=x+dxs[dir],y+dys[dir]
                    if (x,y,dir) not in cnt:
                        if (x,y,dir) in visited:
                            break
                        else:
                            store.append(((x,y,dir),time))
                            visited.add((x,y,dir))
                    else:
                            time+=cnt[(x,y,dir)]
                            max_val=max(max_val,time)
                            break
    

                elif grid[nx][ny]==1:
                    x,y=x+dxs[dir],y+dys[dir]
                    dir=detect_1(dir,nx,ny)
                    if (x,y,dir) not in cnt:
                        if (x,y,dir) in visited:
                            break
                        else:
                            store.append(((x,y,dir),time))
                            visited.add((x,y,dir))
                    else:
                            time+=cnt[(x,y,dir)]
                            max_val=max(max_val,time)
                            break
    

                elif grid[nx][ny]==2:
                    x,y=x+dxs[dir],y+dys[dir]
                    dir=detect_2(dir,nx,ny)
                    if (x,y,dir) not in cnt:
                        if (x,y,dir) in visited:
                            break
                        else:
                            store.append(((x,y,dir),time))
                            visited.add((x,y,dir))
                    else:
                            time+=cnt[(x,y,dir)]
                            max_val=max(max_val,time)
                            break
    

    for state, visited_time in store:
        cnt[state] = time - visited_time

print(max_val)