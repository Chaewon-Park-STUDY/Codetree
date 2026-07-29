n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.

arr=[chr(_) for _ in range(65,65+n)]

new=[]

for i in range(p-1,m):
    if c[i] not in new:
        new.append(c[i])

for j in range(p-1):
    if u[j]==u[p-1]:
        new.append(c[j])

final=[]
for elem in arr:
    if elem not in new:
        final.append(elem)
final.sort()

if u[p-1]!=0:
    for _ in final:
        print(_, end=" ")

