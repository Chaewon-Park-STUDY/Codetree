n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
num=[[-10**10 for _ in range(m)] for _ in range(n)]

num[0][0]=1
start=num[0][0]


for i in range(1,n):
    for j in range(1,m):
        x=grid[i][j]
        for k in range(i):
            for l in range(j):
                if x>grid[k][l]:
                    num[i][j]=max(num[i][j],num[k][l]+1)


max_val=0

for elem in num:
    for _ in elem:
        max_val=max(max_val,_)
print(max_val)