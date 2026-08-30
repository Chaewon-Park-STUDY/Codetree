n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

store=[]
def print_max(visited):
    max_val=1000000
    for i in range(n):
        max_val=min(max_val,grid[i][visited[i]])
    
    store.append(max_val)


visited=[]

def choose(n):
    if len(visited)==n:
        return print_max(visited)
    
    for i in range(n):
        if i not in visited:
            visited.append(i)
            choose(n)
            visited.pop()
choose(n)

print(max(store))