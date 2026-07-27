n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
arr=[0 for _ in range(100)]

for i in range(n):
    for j in range(l[i],r[i]):
        arr[j]+=i+1

num=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            new=arr.copy()
            for _ in range(l[i],r[i]):
                new[_]-=i+1
            for _ in range(l[j],r[j]):
                new[_]-=j+1
            for _ in range(l[k],r[k]):
                new[_]-=k+1
            if any(new[s]>=1 and new[s+1]!=0 and new[s+1]!=new[s] for s in range(99)):
                pass
            else:
                num+=1
print(num)
