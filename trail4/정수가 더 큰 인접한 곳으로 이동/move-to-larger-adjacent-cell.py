n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
x,y=r,c
dxs,dys=[-1,1,0,0],[0,0,-1,1] #북남서동

def in_range(x,y):
    return 1<=x and x<=n and 1<=y and y<=n

is_continue=True
store=[]
store.append(a[x][y])

while is_continue:
    num=0
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and a[nx][ny]>a[x][y]:
            x,y=x+dxs[dir],y+dys[dir]
            store.append(a[x][y])
            num+=1
            break
        else:
            continue
    if num==0:
        is_continue=False

for elem in store:
    print(elem, end=" ")

    








    