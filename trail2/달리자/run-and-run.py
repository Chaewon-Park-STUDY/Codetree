n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

dist=0
for i in range(n-1):
    if A[i]>B[i]:
        A[i+1]+=A[i]-B[i]
        dist+=A[i]-B[i]
        A[i]=B[i]
print(dist)