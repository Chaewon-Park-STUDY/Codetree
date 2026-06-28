N = int(input())

# Please write your code here.

def calculation(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return calculation(n-1)+ n//3
print(calculation(N))
    