n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.

store=[]
pos={}
path={}

for i in range(n):
    for j in range(n):
        if grid[i][j]=="S":
            pos["S"]=(i,j)
        elif grid[i][j]=="E":
            pos["E"]=(i,j)
        elif grid[i][j]!=".":
            if grid[i][j] not in store:
                path[grid[i][j]]=[]
                store.append(grid[i][j])
            path.get(grid[i][j]).append((i,j))

k=len(store)


def dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


min_val=10**8
def print_answer(arr):
    global min_val
    for i in range(len(path.get(arr[0]))):
        for j in range(len(path.get(arr[1]))):
            for k in range(len(path.get(arr[2]))):
                total=(dist(pos.get("S"),path.get(arr[0])[i])
                +dist(path.get(arr[0])[i],path.get(arr[1])[j])
                +dist(path.get(arr[1])[j],path.get(arr[2])[k])
                +dist(path.get(arr[2])[k],pos.get("E")))
                min_val=min(min_val,total)
    
arr=[]

store.sort()

start=0

def choose(k,start):
    if len(arr)==3:
        return print_answer(arr)
    
    for i in range(start,k):
        arr.append(store[i])
        start=i
        choose(k,start+1)
        arr.pop()
choose(k,start)


if min_val==10**8:
    min_val=-1
print(min_val)

