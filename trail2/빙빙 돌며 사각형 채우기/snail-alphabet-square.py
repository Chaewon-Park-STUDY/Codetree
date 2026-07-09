n, m = map(int, input().split())

# Please write your code here.
# chr(65)=A

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

x,y=0,0
dir_num=0
dxs,dys=[0,1,0,-1],[1,0,-1,0] #오른쪽, 아래, 왼쪽, 위

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

arr[x][y]= chr(65)  #ord(Z)= 90

for i in range(1,n*m):
    nx,ny= x+dxs[dir_num], y+dys[dir_num]

    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num= (dir_num+1)%4
    x,y= x+dxs[dir_num], y+dys[dir_num]
    if i>=26:
        arr[x][y]=chr(65+ i%26)
    else:
        arr[x][y]= chr(65+i)

for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()