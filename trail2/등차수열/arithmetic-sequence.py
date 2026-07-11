n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

#n-1개의 칸에 K가 위치할 수 있음
store=[]
for i in range(1,101):
    cnt=0
    for j in range(n-1):
        for k in range(j+1,n):
            if a[j]-i==i-a[k]:
                cnt+=1
    if cnt>=1:
        store.append(cnt)
print(max(store))
    
