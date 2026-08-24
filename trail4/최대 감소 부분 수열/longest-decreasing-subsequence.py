n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

dp=[0 for _ in range(n)]
dp[n-1]=1



for i in range(n-2,-1,-1):
    max_val=0
    for j in range(i+1,n):
        if m[j]<m[i]:
            max_val=max(max_val,dp[j])
    dp[i]=max_val+1
print(max(dp))

