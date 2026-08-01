n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_val=0
for i in range(n-2):
    for k in range(n-2):
        num=0
        for j in range(k,k+3):
            for p in range(3):
                if grid[i+p][j]==1:
                    num+=1
        max_val= max(max_val,num)
print(max_val)


