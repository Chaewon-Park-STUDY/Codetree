n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

dxs,dys=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

start=num[r-1][c-1]

dir={}
for i in range(1,9):
    dir[i]=i-1

start_dir=dir[move_dir[r-1][c-1]] #숫자로 변환



visited=[0 for _ in range(n**2+1)]

for i in range(n**2-1,0,-1):
    arr=[]
    for j in range(n):
        for k in range(n):
            if num[j][k]==i:
                for l in range(1,n):
                    x,y=j,k
                    start=num[x][y]
                    start_dir=dir[move_dir[x][y]]
                    nx,ny=x+l*dxs[start_dir],y+l*dys[start_dir]
                    if in_range(nx,ny) and num[nx][ny]>start:
                        arr.append(visited[num[nx][ny]])
    if len(arr)>0:
        visited[i]=max(arr)+1

print(visited[num[r-1][c-1]])

