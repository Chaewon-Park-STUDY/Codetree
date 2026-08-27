n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

dp=[100 for _ in range(n)]
dp[0]=0

for i in range(1,n):
    min_val=10000
    for j in range(i):
        if i-j<=num[j]:
            dp[i]=min(dp[i],dp[j]+1)
            min_val=min(min_val,dp[i])
    dp[i]=min_val


if dp[n-1]!=10000:
    print(dp[n-1])
else:
    print(-1)