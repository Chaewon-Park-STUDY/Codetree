n = int(input())

# Please write your code here.

memo=[-1 for _ in range(n)]
def fibbo(n):
    if memo[n-1]!=-1:
        return memo[n-1]
    if n==1:
        memo[n-1]=1
    elif n==2:
        memo[n-1]=2
    else:
        memo[n-1]=fibbo(n-1)+fibbo(n-2)
    return memo[n-1]
print(fibbo(n)%10007)