n, m = map(int, input().split())

# Please write your code here.

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]



def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

num=1
for i in range(m):
    x,y=0,i
    arr[x][y]=num
    while True:
        nx,ny=x+1,y-1
        if in_range(nx,ny):
            x,y=x+1,y-1
            num+=1
            arr[x][y]=num
        else:
            num+=1
            break




for j in range(n-1):
    x,y=j+1,m-1
    arr[x][y]=num
    while True:
        nx,ny=x+1,y-1
        if in_range(nx,ny):
            if arr[nx][ny]==0:
                x,y=x+1,y-1
                num+=1
                arr[x][y]=num
        else:
            num+=1
            break

for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()