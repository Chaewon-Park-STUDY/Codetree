n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.

dp=[[] for _ in range(n)]

if numbers[0]>=0:
    dp[0]=[(numbers[0],0)]
else:
    dp[0]=[(numbers[0],1)]

for i in range(1,n):
    arr=dp[i-1]
    for elem in arr:
        (x,y)=elem
        if numbers[i]>=0:
                dp[i].append((x+numbers[i],y))
                dp[i].append((numbers[i],0))
        else:
            if y<k:
                dp[i].append((max(numbers[i],x+numbers[i]),y+1))
            dp[i].append((numbers[i], 1)) 
        
    best={}
    for (x,y) in dp[i]:
        best[y]=max(best.get(y,-10**5),x)
    dp[i] = [(best[key], key) for key in best]

max_val=-10**8
for elem in dp:
    for _ in elem:
        (x,y)=_
        max_val=max(max_val,x)
print(max_val)