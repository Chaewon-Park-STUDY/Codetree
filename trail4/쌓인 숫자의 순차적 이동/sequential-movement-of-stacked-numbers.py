n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

# Please write your code here.

dxs,dys=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

cnt={}
for i in range(n):
    for j in range(n):
        cnt[(i,j)]=[grid[i][j]]

for i in range(m):
    a=move_nums[i]
    group=[]
    for pos in cnt:
        if a in cnt.get(pos):
            x,y=pos[0],pos[1]
            for j in range(len(cnt.get(pos))):
                if cnt.get(pos)[j]==a:
                    for elem in cnt.get(pos)[0:j+1]:
                        group.append(elem)

    max_val=0
    for k in range(8):
        dir=k
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and len(cnt.get((nx,ny)))>0:
            max_val=max(max_val,max(cnt.get((nx,ny))))
    if max_val>0:
        for pos in cnt:
            if all(elem in cnt.get(pos) for elem in group):
                for l in range(len(group)):
                    cnt.get(pos).pop(0)

    for pos in cnt:
        if max_val in cnt.get(pos):
            for j in range(len(group)):
                cnt.get(pos).insert(j,group[j])


for i in range(n):
    for j in range(n):
        if len(cnt[(i,j)])==0:
            print("None")
        else:
            for elem in cnt.get((i,j)):
                print(elem, end=" ")
            print()