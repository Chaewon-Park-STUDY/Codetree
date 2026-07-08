R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

starting_point=grid[0][0]
ending_point= grid[R-1][C-1]
x,y=0,0
path=[]
second=[]
on=True

if starting_point=="W" and ending_point!="W":
    while on:
        num=0
        for i in range(1,R-1):
            for j in range(1,C-1):
                if grid[i][j]!="W":
                    x,y=i,j
                    num+=1
                    path.append((x,y))
                    for k in range(i+1,R-1):
                        for l in range(j+1,C-1):
                            if grid[k][l]=="W":
                                x,y=k,l
                                num+=1
                                second.append((x,y))
                                on=False

if starting_point=="B" and ending_point!="B":
    while on:
        num=0
        for i in range(1,R-1):
            for j in range(1,C-1):
                if grid[i][j]!="B":
                    x,y=i,j
                    num+=1
                    path.append((x,y))
                    for k in range(i+1,R-1):
                        for l in range(j+1,C-1):
                            if grid[k][l]=="B":
                                x,y=k,l
                                num+=1
                                second.append((x,y))
                                on=False



print(len(second))
