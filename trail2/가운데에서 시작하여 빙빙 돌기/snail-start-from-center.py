n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
x,y= int((n-1)/2),int((n-1)/2)
dir_num=0
dxs,dys=[0,-1,0,1],[1,0,-1,0]  #순서대로 오른쪽, 위쪽, 왼쪽, 아래쪽
grid[x][y]= 1


step=1
for i in range(2,2*n+1):
    if i%2==0 and i!=2*n:
        for j in range(int(i/2)):
            step+=1
            x,y= x+dxs[dir_num], y+dys[dir_num]
            grid[x][y]=step
        dir_num= (dir_num+1)%4

    elif i%2!=0:
        for j in range(int((i-1)/2)):
            step+=1
            x,y= x+dxs[dir_num], y+dys[dir_num]
            grid[x][y]=step
        dir_num= (dir_num+1)%4


    else:
        for j in range(n-1):
            step+=1
            x,y= x+dxs[dir_num], y+dys[dir_num]
            grid[x][y]= step

for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()


