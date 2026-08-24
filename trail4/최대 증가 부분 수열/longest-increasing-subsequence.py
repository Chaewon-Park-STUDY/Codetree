n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp=[0 for _ in range(n)]

dp[0]=1


for i in range(1,n):
    max_val=0
    for j in range(i):
        if m[j]<m[i]:
            max_val=max(max_val,dp[j])
    dp[i]=max_val+1
print(max(dp))