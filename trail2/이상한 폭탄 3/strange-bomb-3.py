N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

max_val=0
store=[]
for i,elem in enumerate(num):
    dist=[]
    if num.count(elem)>1:
        dist.append(i)
        for j in range(i+1,N):
            if num[j]==elem:
                if j-i<=K:
                    dist.append(j)
        max_val= max(max_val,len(dist))
        if len(dist)!=1 and len(dist)==max_val:
            store.append((max_val,i))

if len(store)>0:
    for elem in store:
        if elem[0]==max_val:
            print(num[elem[1]])
            break
else:
    print(0)