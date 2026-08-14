T = int(input())

def in_range(x,y):
    return 1<=x and x<N+1 and 1<=y and y<N+1
dxs,dys=[-1,1,0,0],[0,0,1,-1] #U,D,R,L
dir=0


def direction(dir):
    if dir=="U":
        dir=0
    elif dir=="D":
        dir=1
    elif dir=="R":
        dir=2
    else:
        dir=3
    return dir

def convert(dir):
    if dir==0:
        dir="U"
    elif dir==1:
        dir="D"
    elif dir==2:
        dir="R"
    else:
        dir="L"
    return dir


for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)
    num=M
    remain=0
    if M==0:
        print(0)
    while num>0:
        store=[]
        for i in range(num):
            start_x,start_y=x[i],y[i]
            dir=direction(d[i])
            nx,ny=start_x+dxs[dir],start_y+dys[dir]
            if in_range(nx,ny):
                start_x,start_y=start_x+dxs[dir],start_y+dys[dir]
                store.append((start_x,start_y))
                x[i],y[i]=start_x,start_y
                d[i]=convert(dir)
            else:
                if dir%2==0:
                    dir+=1
                else:
                    dir-=1
                store.append((start_x,start_y))
                x[i],y[i]=start_x,start_y
                d[i]=convert(dir)
        cnt={}
        arr=[]
        for pos in store:
            cnt[pos]=cnt.get(pos,0)+1
        
        for i in range(len(store)):
            if cnt[store[i]]==1:
                arr.append(i)
        
       
        new_x,new_y,new_dir=[],[],[]
        for elem in arr:
                new_x.append(x[elem])
                new_y.append(y[elem])
                new_dir.append(d[elem])
        x,y,d=new_x,new_y,new_dir
        
        if len(arr)==num:
            remain+=1
            if remain>=2*N:
                print(len(arr))
                break
        if len(arr)==0:
            print(len(arr))
            break
        num=len(arr)
