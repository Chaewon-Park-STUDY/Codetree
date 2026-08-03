n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


max_val=0
#세로 방향
for i in range(n):
    for j in range(m-2):
        sum_val=0
        for k in range(j,j+3):
            sum_val+=grid[i][k]
        max_val=max(max_val,sum_val)

for i in range(m):
    for j in range(n-2):
        sum_val=0
        for k in range(j,j+3):
            sum_val+=grid[k][i]
        max_val=max(max_val,sum_val)

#
for i in range(n-1):
    for j in range(m-1):
        store=[]
        for l in range(2):
            for k in range(2):
                store.append(grid[i+l][j+k])
        for q in range(4):
            sum_val=0
            for p in range(4):
                if p!=q:
                    sum_val+=store[p]
            max_val=max(max_val,sum_val)
       

print(max_val) 


