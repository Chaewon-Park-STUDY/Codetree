inp = [input() for _ in range(3)]

# Please write your code here.
total=[]

#가로
for i in range(3):
    store=[]
    for j in range(3):
        if inp[i][j] not in store:
            store.append(inp[i][j])
    if len(store)==2:
        store.sort()
        if store not in total:
            total.append(store)

#세로
for i in range(3):
    store=[]
    for j in range(3):
        if inp[j][i] not in store:
            store.append(inp[j][i])
    if len(store)==2:
        store.sort()
        if store not in total:
            total.append(store)

#대각선
store=[]
for i in range(3):
    if inp[i][i] not in store:
        store.append(inp[i][i])
if len(store)==2:
    store.sort()
    if store not in total:
        total.append(store)

new=[]
for i in range(3):
    if inp[i][2-i] not in new:
        new.append(inp[i][2-i])
if len(new)==2:
    new.sort()
    if new not in total:
        total.append(new)
print(len(total))


