n, m, t = map(int, input().split())

r = []
c = []
d = []
w = []

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    w.append(int(wi))

# Please write your code here.

def in_range(x,y):
    return 1<=x and x<n+1 and 1<=y and y<n+1

dxs,dys=[-1,1,0,0],[0,0,1,-1]     # U, D, R, L

def direction(dir):
    if dir=="U":
        return 0
    elif dir=="D":
        return 1
    elif dir=="R":
        return 2
    else:
        return 3

def convert(dir):
    if dir==0:
        return "U"
    elif dir==1:
        return "D"
    elif dir==2:
        return "R"
    else:
        return "L"



time=t
num=m #나중에 while loop를 돌면서 num=len(arr)으로 바뀜
while time>0:
    store=[]
    for i in range(num):
        x,y=r[i],c[i]
        dir=direction(d[i])
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny):
            x,y=x+dxs[dir],y+dys[dir]
            r[i],c[i]=x,y
            d[i]=convert(dir)
            store.append((x,y))
        else:
            if dir%2==0:
                dir+=1
            else:
                dir-=1
            d[i]=convert(dir)
            store.append((x,y))

    cnt={}
    arr=[]
    for pos in store:
        cnt[pos]=cnt.get(pos,0)+1
    max_index={}
    weight={}
    for pos in store:
        max_index[pos]=0

    for i in range(len(store)):
        if cnt[store[i]]==1:
            arr.append(i)
        else:
            max_index[store[i]]=i
    for i in range(len(store)):
        if cnt[store[i]]>1 and max_index[store[i]]==i:
            arr.append(i)

    for i in range(len(store)):
        weight[store[i]]=weight.get(store[i],0)+w[i]
    new_x,new_y,new_dir,new_weight=[],[],[],[]
    arr.sort()
    for elem in arr:
        new_x.append(r[elem])
        new_y.append(c[elem])
        new_dir.append(d[elem])
        new_weight.append(weight.get(store[elem]))
    r,c,d,w=new_x,new_y,new_dir,new_weight
    num=len(arr) 

    time-=1
    if time==0:
        print(len(arr),max(w))
        break
        


