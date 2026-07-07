n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_sum=0
for i in range(n):
    for k in range(n-2):
        sum_value=0
        for j in range(k,k+3):
            sum_value+=grid[i][j]
        if sum_value>=max_sum:
            max_sum= sum_value
print(max_sum)