n = int(input())

# Please write your code here.


dp=[1 for _ in range(10)]
dp[0]=1

if n>=2:
    for i in range(1,9):
        dp[i]=2


for i in range(n-2):
    new_dp=[0]*10

    new_dp[0] = dp[1]
    new_dp[9] = dp[8]

    for i in range(1, 9):
        new_dp[i] = dp[i-1]+dp[i+1]
    dp=new_dp

a=sum(dp[1:])

print(a%(10**9+7))