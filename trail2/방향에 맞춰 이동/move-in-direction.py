n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x,y=0,0
dx,dy= [1,0,-1,0], [0,-1,0,1]

for i in range(n):
    if dir[i]== "N":
        x,y= x+ dx[3]*dist[i], y+ dy[3]*dist[i]
    elif dir[i]== "E":
        x,y= x+dx[0]*dist[i], y+ dy[0]*dist[i]
    elif dir[i]== "S":
        x,y= x+dx[1]*dist[i], y+ dy[1]*dist[i]
    else:
        x,y= x+dx[2]*dist[i], y+ dy[2]*dist[i]

print(x,y)