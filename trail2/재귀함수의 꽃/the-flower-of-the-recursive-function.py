N = int(input())

# Please write your code here.

def logic(N):
    if N==0:
        return
    print(N, end=" ")
    logic(N-1)
    print(N, end=" ")
logic(N)