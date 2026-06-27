N = int(input())

# Please write your code here.

def Fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return Fibonacci(n-1)+ Fibonacci(n-2)

print(Fibonacci(N))