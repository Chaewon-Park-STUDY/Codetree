N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()



store=[]
for i in range(N-L+1):
    for j in range(i,i+L):
        a[j]+=1
    for p in range(max(a)+1):
        num=0
        for k in range(N):
            if a[k]>=p:
                num+=1
        if num>=p:
            store.append(p)
    for m in range(i,i+L):
        a[m]-=1
print(max(store))