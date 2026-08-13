# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.

if dir=="R":
    for i in range(4):
        store=[]
        start=3
        while start>0:
            if grid[i][start]!=0:
                if grid[i][start]!=grid[i][start-1]:
                    store.append(grid[i][start])
                    start-=1
                    if start==0 and grid[i][0]!=0:
                        store.append(grid[i][0])
                else:
                    store.append(2*grid[i][start])
                    start-=2
                    if start==0 and grid[i][0]!=0:
                        store.append(grid[i][0])
            else:
                start-=1
                if start==0 and grid[i][0]!=0:
                    store.append(grid[i][0])
        
        store.reverse()
        for a in range(0,4-len(store)):
            grid[i][a]=0
        for a in range(4-len(store),4):
            grid[i][a]=store[a-4+len(store)]

elif dir=="L":
    for i in range(4):
        store=[]
        start=0
        while start<3:
            if grid[i][start]!=0:
                if grid[i][start]!=grid[i][start+1]:
                    if start!=2 and grid[i][start+1]==0 and grid[i][start]==grid[i][start+2]:
                        store.append(2*grid[i][start])
                        start+=3
                    else:
                        store.append(grid[i][start])
                        start+=1
                    if start==3 and grid[i][3]!=0:
                        store.append(grid[i][3])
                else:
                    store.append(2*grid[i][start])
                    start+=2
                    if start==3 and grid[i][3]!=0:
                        store.append(grid[i][3])
            else:
                start+=1
                if start==3 and grid[i][3]!=0:
                    store.append(grid[i][3])
    
        for a in range(len(store)):
            grid[i][a]=store[a]

        for a in range(len(store),4):
            grid[i][a]=0



elif dir=="U":
    for i in range(4):
        store=[]
        start=0
        while start<3:
            if grid[start][i]!=0:
                if grid[start][i]!=grid[start+1][i]:
                    store.append(grid[start][i])
                    start+=1
                    if start==3 and grid[3][i]!=0:
                        store.append(grid[3][i])
                else:
                    store.append(2*grid[start][i])
                    start+=2
                    if start==3 and grid[3][i]!=0:
                        store.append(grid[3][i])
            else:
                start+=1
                if start==3 and grid[3][i]!=0:
                    store.append(grid[3][i])
    
        for a in range(len(store)):
            grid[a][i]=store[a]

        for a in range(len(store),4):
            grid[a][i]=0
else:
    for i in range(4):
        store=[]
        start=3
        while start>0:
            if grid[start][i]!=0:
                if grid[start][i]!=grid[start-1][i]:
                    if start!=1 and grid[start-1][i]==0 and grid[start][i]==grid[start-2][i]:
                        store.append(2*grid[start][i])
                        start-=3
                    else:
                        store.append(grid[start][i])
                        start-=1
                    if start==0 and grid[0][i]!=0:
                        store.append(grid[0][i])
                else:
                    store.append(2*grid[start][i])
                    start-=2
                    if start==0 and grid[0][i]!=0:
                        store.append(grid[0][i])
            else:
                start-=1
                if start==0 and grid[0][i]!=0:
                    store.append(grid[0][i])
        
        store.reverse()
        for a in range(0,4-len(store)):
            grid[a][i]=0
        for a in range(4-len(store),4):
            grid[a][i]=store[a-4+len(store)]

for elem in grid:
    for _ in elem:
        print(_, end=" ")
    print()