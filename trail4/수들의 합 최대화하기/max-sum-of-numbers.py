n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_val=0
def print_max(arr):
    total=0
    for i in range(n):
        total+=grid[i][arr[i]]

    global max_val
    max_val=max(max_val,total)



picked=[]

start=0
def choose(n):
    if len(picked)==n:
        return print_max(picked)
    for j in range(0,n):
        if j not in picked:
            picked.append(j)
            choose(n)
            picked.pop()
choose(n)
print(max_val)

