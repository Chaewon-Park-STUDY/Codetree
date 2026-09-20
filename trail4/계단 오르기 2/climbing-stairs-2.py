n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.

dp=[[] for _ in range(n+1)]
dp[1].append((coin[1],1))
dp[2].append((coin[2],0))
dp[2].append((coin[1]+coin[2],2))

if n>=3:
    for i in range(3,n+1):
        arr=dp[i-2]
        for elem in arr:
            (x,y)=elem
            if y<=3:
                dp[i].append((x+coin[i],y))
        store=dp[i-1]
        for elem in store:
            (x,y)=elem
            if y<3:
                dp[i].append((x+coin[i],y+1))
        best={}
        for x, y in dp[i]:
            best[y] = max(best.get(y, -1), x)
        dp[i] = [(best[key], key) for key in best]


dp[n].sort()
print(dp[n][-1][0])