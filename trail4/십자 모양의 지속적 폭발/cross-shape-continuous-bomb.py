n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n



num=0
while num<m:
    b=commands[num]-1
    for j in range(n):
        if grid[j][b]!=0:
            start=grid[j][b]
            for k in range(1,start):
                    if in_range(j-k,b):
                        grid[j-k][b]=0
                    if in_range(j+k,b):
                        grid[j+k][b]=0
                    if in_range(j,b-k):
                        grid[j][b-k]=0
                    if in_range(j,b+k):
                        grid[j][b+k]=0
            grid[j][b]=0
            break
    for l in range(n):
        zero_count=0
        for a in range(n):
            if grid[a][l]==0:
                zero_count+=1
        new=[]
        for a in range(n-1):
            if grid[a][l]!=0:
                new.append(grid[a][l])

        for a in range(n-1):
            if a<zero_count:
                grid[a][l]=0
        for k in range(len(new)):
                grid[zero_count+k][l]=new[k]
    num+=1


for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()
