N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x,y=0,0
dxs,dys= [1,0,-1,0], [0,-1,0,1] #순서대로 오른쪽 아래, 왼쪽, 위
store={}
store["E"]=0
store["S"]=1
store["W"]=2
store["N"]=3

game_is_on=True

new=[]
all_time=[]
time=0
for i in range(N):
    dir_num= store[dir[i]]
    for j in range(dist[i]):
        nx,ny= dxs[dir_num], dys[dir_num]
        time+=1
        x,y= x+nx,y+ny
        new.append((x,y))
        if x==0 and y==0:
            all_time.append(time)
            break
num=0
for elem in new:
    if elem== (0,0):
        num+=1
if num!=0:
    print(all_time[0])
else:
    print(-1)


