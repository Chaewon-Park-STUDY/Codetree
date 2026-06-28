N = int(input())

# Please write your code here.

def calculation(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (calculation(n-1)*calculation(n-2))%100
print(calculation(N))