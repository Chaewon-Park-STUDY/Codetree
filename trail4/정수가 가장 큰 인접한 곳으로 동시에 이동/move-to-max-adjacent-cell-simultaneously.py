n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.

#북,남,서,동

dxs,dys=[-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
for k in range(m):
    r[k]-=1
    c[k]-=1

time=0
arr=[i for i in range(m)]

while time<=t:
    store=[]
    index=[]
    for j in range(m):
        if j in arr:
            new=[]
            coor=[]
            for k in range(4):
                dir=k
                x,y=r[j],c[j]
                nx,ny=x+dxs[dir],y+dys[dir]
                if in_range(nx,ny):
                    x,y=x+dxs[dir],y+dys[dir]
                    if a[nx][ny] not in new:
                        new.append((a[nx][ny]))
                        coor.append((x,y))
        
            for l in range(len(new)):
                if new[l]==max(new):
                    r[j]=coor[l][0]
                    c[j]=coor[l][1]
        
            store.append((r[j],c[j]))
            index.append(j)
    arr=[]
    for p in range(len(store)):
        if store.count(store[p])>=2:
            pass
        else:
            arr.append(index[p])
    time+=1
    if time==t:
        break


print(len(arr))
