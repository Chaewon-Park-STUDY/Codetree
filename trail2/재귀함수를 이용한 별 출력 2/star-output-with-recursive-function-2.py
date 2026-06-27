n = int(input())

# Please write your code here.

def logic(n):
    if n==0:
        return
    for i in range(n):
        print("*", end=" ")
    print()
    logic(n-1)
    for i in range(n):
        print("*", end=" ")
    print()

logic(n)