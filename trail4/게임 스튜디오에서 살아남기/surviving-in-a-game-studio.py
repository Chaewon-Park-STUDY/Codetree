n = int(input())

# Please write your code here.
dp=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]

dp[1][0][0] = 1  # G
dp[1][0][1] = 1  # B
dp[1][1][0] = 1  # T

for i in range(2, n + 1):
    for t in range(3):
        for b in range(3):
            c = dp[i - 1][t][b]
            dp[i][t][0] += c          # G 붙이기
            if b < 2:
                dp[i][t][b + 1] += c  # B 붙이기
            if t < 2:
                 dp[i][t + 1][0] += c  # T 붙이기
num=0

for elem in dp[n]:
    num+=sum(elem)
print(num%(10**9+7))