N = int(input())

# Please write your code here.


memo=[-1 for _ in range(N)]

def repeat(N):
    if memo[N-1]!=-1:
        return memo[N-1]
    if N<=2:
        memo[N-1]=1
        return 1
    else:
        memo[N-1]=repeat(N-1)+repeat(N-2)
        return repeat(N-1)+repeat(N-2)
    
print(repeat(N))
