n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys=[-1,-1,1,1],[1,-1,-1,1]


store=[]
for i in range(n):
    for j in range(n):
        for k in range(1,n-1): 
            x,y=i,j
            dir=0
            sum_val=0
            if in_range(x+k*dxs[dir],y+k*dys[dir]):
                for p in range(k):
                    nx,ny=x+dxs[dir],y+dys[dir]
                    sum_val+=grid[nx][ny]
                    x,y=x+dxs[dir],y+dys[dir]
                new_x,new_y=x,y
                
                for l in range(1,n-1):
                    x,y=new_x,new_y
                    dir=1
                    arr=sum_val
                    if in_range(x+l*dxs[dir],y+l*dys[dir]):
                        for z in range(l):
                            nx,ny=x+dxs[dir],y+dys[dir]
                            arr+=grid[nx][ny]
                            x,y=x+dxs[dir],y+dys[dir]
                        dir=2
                        if in_range(x+k*dxs[dir],y+k*dys[dir]):
                            for t in range(k):
                                nx,ny=x+dxs[dir],y+dys[dir]
                                arr+=grid[nx][ny]
                                x,y=x+dxs[dir],y+dys[dir]
                            dir=3
                            if in_range(x+l*dxs[dir],y+l*dys[dir]): 
                                for q in range(l):
                                        nx,ny=x+dxs[dir],y+dys[dir]
                                        arr+=grid[nx][ny]
                                        x,y=x+dxs[dir],y+dys[dir]
                                store.append(arr)

                            
print(max(store))
                        








