N = int(input())

# Please write your code here.

def factorial(n):
    if n==1:
        return 1
    return factorial(n-1) * n
print(factorial(N))