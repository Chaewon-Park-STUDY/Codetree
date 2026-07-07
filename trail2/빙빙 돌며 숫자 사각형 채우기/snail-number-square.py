n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0          
dir_num = 0       # 방향은 순서대로 오른쪽, 아래쪽, 왼쪽, 위쪽     

arr[x][y]=1

for i in range(2,n*m+1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num= (dir_num+1)%4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for elem in arr:
    for i in elem:
        print(i, end=" ")
    print()