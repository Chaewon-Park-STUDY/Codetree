n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def calculation(N,M):
    total=A[M-1]
    while M!=1:
        if M%2!=0:
            M-=1
            total+=A[M-1]
            if M==1:
                break
        else:
            M= int(M/2)
            total+=A[M-1]
            if M==1:
                break
    return total

print(calculation(n,m))