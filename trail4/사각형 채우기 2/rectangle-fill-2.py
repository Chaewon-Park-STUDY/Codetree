n = int(input())

# Please write your code here.

memo = [-1 for _ in range(n + 1)]

def f(n):
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]

    total = 0
    for i in range(1, n):
        total += f(i)

    if n%2==0:
        memo[n] = total + 2
    else:
        memo[n] = total + 1

    return memo[n]

print(f(n)%10007)