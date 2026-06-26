n = int(input())

# Please write your code here.

def logic(n):
    if n==0:
        return
    logic(n-1)
    print("*"*n)

logic(n)