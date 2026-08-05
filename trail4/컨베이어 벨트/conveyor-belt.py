n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

arr=[]

for elem in u:
    arr.append(elem)
for elem in d:
    arr.append(elem)

store=arr.copy()
for i in range(t):
    new=[]
    new.append(store[-1])
    for elem in store[0:2*n-1]:
        new.append(elem)
    store=new.copy()


for elem in store[0:n]:
    print(elem, end=" ")
print()
for _ in store[n:2*n]:
    print(_, end=" ")