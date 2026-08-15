n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

# Please write your code here.

time=t

dxs,dys=[-1,1,0,0],[0,0,1,-1]

def direction(dir):
    if dir=="U":
        return 0
    elif dir=="D":
        return 1
    elif dir=="R":
        return 2
    else:
        return 3

def in_range(x,y):
    return 1<=x and x<=n and 1<=y and y<=n


def change(dir):
    if dir%2==0:
        dir+=1
    else:
        dir-=1
    return dir

def convert(dir):
    if dir==0:
        return "U"
    elif dir==1:
        return "D"
    elif dir==2:
        return "R"
    else:
        return "L"

num=m
while time>0:
    store=[]
    for i in range(num):
        x,y=r[i],c[i]
        dir=direction(d[i])
        for j in range(v[i]):
            nx,ny=x+dxs[dir],y+dys[dir]
            if not in_range(nx,ny):
                dir=change(dir)
            x,y=x+dxs[dir],y+dys[dir]
        store.append((x,y))
        r[i],c[i]=x,y
        d[i]=convert(dir)
    arr={}
    new=[]
    for elem in store:
        if elem not in new:
            new.append(elem)
    for pos in new:
        arr[pos]=[]

    for i in range(len(store)):
        for key in arr:
            if key==store[i]:
                arr[key].append(i)
    on_going=[]
    for pos in arr:
        if len(arr[pos])<=k:
            for elem in arr[pos]:
                on_going.append(elem)
        else:
            tray=[]
            for elem in arr[pos]:
                tray.append((v[elem],elem))
            tray.sort()
            tray.reverse()
            for elem in tray[0:k]:
                on_going.append(elem[1])
    new_r,new_c,new_d,new_v=[],[],[],[]
    on_going.sort()
    for elem in on_going:
        new_r.append(r[elem])
        new_c.append(c[elem])
        new_d.append(d[elem])
        new_v.append(v[elem])
    r,c,d,v=new_r,new_c,new_d,new_v

    num=len(on_going)
    time-=1
    if time==0:
        print(num)
    