N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

dp=[10000 for _ in range(M+1)]
dp[0]=0

for i in range(1,M+1):
    min_val=10**7
    for j in range(N):
        if coin[j]<=i:
            min_val=min(min_val,dp[i-coin[j]]+1)
    dp[i]=min_val


if dp[-1]==10**7:
    print(-1)
else:
    print(dp[-1])