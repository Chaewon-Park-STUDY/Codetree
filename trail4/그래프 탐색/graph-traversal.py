n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

visited=[]
check=[0 for _ in range(m)] #확인해야할 edges

for i in range(m):
    if 1 in edges[i]:
        for _ in edges[i]:
            if _!=1 and _ not in visited:
                visited.append(_)
                check[i]="X"
def adding(store):
    for elem in store:
        if elem in visited:
            return True

is_continue=True

while is_continue:
    num=check.count("X")
    for i in range(m):
        if check[i]!="X":
            if adding(edges[i]):
                for elem in edges[i]:
                    if elem not in visited:
                        visited.append(elem)
                        check[i]="X"
    if num==check.count("X"):
        is_continue=False
        break

print(len(visited))