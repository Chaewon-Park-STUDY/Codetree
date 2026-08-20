N, M, K = map(int, input().split())

x, y = [], []
for _ in range(M):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d, p = [], []
for _ in range(K):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))

# Please write your code here.
store=[]
def in_range(x,y):
    return 1<=x and x<=N and 1<=y and y<=N
store.append([1,1])
dxs,dys=[-1,1,0,0],[0,0,1,-1]

apple=set()
for i in range(M):
    apple.add((x[i],y[i]))


def move(pos_x,pos_y,dir):
    if dir=="U":
        dir=0
    elif dir=="D":
        dir=1
    elif dir=="R":
        dir=2
    else:
        dir=3

    nx,ny=pos_x+dxs[dir],pos_y+dys[dir]
    return [nx,ny]

remove_list=set()
time=0
is_continue=True

for i in range(K):
    for j in range(p[i]):
        time+=1
        new=[]
        for elem in store:
            pos_x,pos_y=elem[0],elem[1]
            new.append(move(pos_x,pos_y,d[i]))
            break
        for z in range(len(store)-1):
            new.append(store[z])
        head_x,head_y=new[0][0],new[0][1]
        if not in_range(head_x,head_y):
            is_continue=False
            
        if (head_x,head_y) in apple:
            apple.remove((head_x,head_y))
            new.append(store[-1])
        if M>0:
            for q in range(2,len(new)):
                if head_x==new[q][0] and head_y==new[q][1]:
                    is_continue=False
                
        store=new
        if is_continue==False:
            break
    if is_continue==False:
        break
            

print(time)





