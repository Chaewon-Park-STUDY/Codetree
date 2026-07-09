n, m = map(int, input().split())

# Please write your code here.
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
x,y=0,0
arr=[
    [0 for _ in range (m)]
    for _ in range (n)
]

dxs,dys= [1,0,-1,0],[0,1,0,-1]  #순서대로 아래 오른쪽 위 왼쪽
dir_num=0 # 0  1 2 3 

arr[x][y]=1


for i in range(2,n*m+1):
    nx,ny= x+dxs[dir_num], y+dys[dir_num]

    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num= (dir_num+1)%4
    
    x,y= x+dxs[dir_num], y+dys[dir_num]
    arr[x][y]=i

for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()