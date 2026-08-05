n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

arr=[]
arr.extend(l+r+d)

store=arr.copy()
for i in range(t):
    new=[]
    new.append(store[-1])
    for elem in store[0:3*n-1]:
        new.append(elem)
    store=new.copy()

for i in range(3):
    for j in range(n*i,n*i+n):
        print(store[j], end=" ")
    print()