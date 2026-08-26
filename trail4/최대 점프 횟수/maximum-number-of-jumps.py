n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

dp=[-10**20 for _ in range(n)] #가장 마지막으로 도착했을 때 최대 횟수
x=0
dp[0]=0

for i in range(1,n):
    for j in range(i):
        if i-j<=arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

