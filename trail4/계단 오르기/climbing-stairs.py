n = int(input())

# Please write your code here.

memo=[0 for _ in range(n-1)]

def stair(n):
    if memo[n-2]!=0:
        return memo[n-2]
    
    if n<=4:
        memo[n-2]=1
        return 1
    elif n==5:
        memo[n-2]=2
        return 2
    else:
        memo[n-2]=stair(n-2)+stair(n-3)
        return stair(n-2)+stair(n-3)

a=stair(n)
print(a%10007)