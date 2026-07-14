N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
arr=[]
for elem in str:
    arr.append(elem)


x,y= (N-1)//2, (N-1)//2
num=board[x][y]
dxs,dys=[-1,0,1,0],[0,1,0,-1] #default가 북쪽이니까 순서대로 북 동 남 서 
dir_num=0

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

for elem in arr:
    if elem=="F":
        nx,ny= x+dxs[dir_num], y+dys[dir_num]
        if in_range(nx,ny):
            x,y=x+dxs[dir_num], y+dys[dir_num]
            num+=board[x][y]
    elif elem=="R":
        dir_num= (dir_num+1)%4
    else:
        dir_num= (dir_num-1+4)%4

print(num)

