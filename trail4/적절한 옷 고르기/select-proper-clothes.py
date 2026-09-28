N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.

grid=[[-1 for _ in range(N)] for _ in range(M)]

def in_range(a,b,x):
    return a-1<=x<=b-1


for i in range(N):
    if s[i]==1:
        grid[0][i]=0

for i in range(1,M):
    for j in range(N):
        max_val=0
        if in_range(s[j],e[j],i):
            for k in range(N):
                if grid[i-1][k]!=-1:
                    max_val=max(max_val,grid[i-1][k]+abs(v[j]-v[k]))
            grid[i][j]=max_val
        


num_total=max(grid[M-1])
print(num_total)
