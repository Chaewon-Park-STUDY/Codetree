N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<M

dxs,dys=[0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1] # 동쪽 방향부터 시작

num=0
for i in range(N):
    for j in range(M):
        start= arr[i][j]
        for k in range(8):
            x,y=i,j
            store=[]
            store.append(start)
            dir=k
            for l in range(2):
                nx,ny= x+dxs[dir],y+dys[dir]
                if in_range(nx,ny):
                    x,y= x+dxs[dir],y+dys[dir]
                    store.append(arr[x][y])
            set1=''
            for elem in store:
                set1+=elem
            if set1=="LEE":
                num+=1
print(num)


