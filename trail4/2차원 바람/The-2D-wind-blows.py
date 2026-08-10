n, m, q = map(int, input().split())

# Create 2D array for building state
arr = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

dxs,dys=[-1,0,1,0],[0,1,0,-1]


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m


for i in range(q):
        new=[]
        store=[]
        a,b,c,d=winds[i][0]-1,winds[i][1]-1, winds[i][2]-1,winds[i][3]-1
        for j in range(b,d):
            new.append(arr[a][j])
        for j in range(a,c):
            new.append(arr[j][d])
        for j in range(d,b,-1):
            new.append(arr[c][j])
        for j in range(c,a,-1):
            new.append(arr[j][b])
        store.append(new[-1])
        for j in new[0:-1]:
            store.append(j)
        num=0
        for j in range(b,d):
            arr[a][j]=store[num]
            num+=1
        for j in range(a,c):
            arr[j][d]=store[num]
            num+=1
        for j in range(d,b,-1):
            arr[c][j]=store[num]
            num+=1
        for j in range(c,a,-1):
            arr[j][b]=store[num]
            num+=1
        final=[]
        count_num=0
        for j in range(a,c+1):
            for k in range(b,d+1):
                x,y=j,k
                sum_val=[]
                sum_val.append(arr[x][y])
                for l in range(4):
                    dir=l
                    nx,ny=x+dxs[dir],y+dys[dir]
                    if in_range(nx,ny):
                        sum_val.append(arr[nx][ny])
                final.append(sum(sum_val)//len(sum_val))
        for j in range(a,c+1):
            for k in range(b,d+1):
                arr[j][k]=final[count_num]
                count_num+=1



for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()