n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

min_val=10**8
def print_cost(visited):
    visited.append(0)
    total=0
    global min_val
    for i in range(n):
        if A[visited[i]][visited[i+1]]==0:
            visited.pop()
            return False
        else:
            total+=A[visited[i]][visited[i+1]]
    min_val=min(min_val,total)
    visited.pop()


visited=[0]

def choose(n):
    if len(visited)==n:
        return print_cost(visited)
    for i in range(1,n):
        if i not in visited:
            visited.append(i)
            choose(n)
            visited.pop()

choose(n)


print(min_val)
