n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.

store=[]

for i in range(1,n+1):
    if a[i] not in store:
        store.append(a[i])


store.sort()

if len(store)==1:
    print(-1)
else:
    if a.count(store[1])>1:
        print(-1)
    else:
        for j in range(1,n+1):
            if a[j]==store[1]:
                print(j)
    