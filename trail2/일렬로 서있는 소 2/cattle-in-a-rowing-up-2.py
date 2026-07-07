N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
num=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i]<=A[j]<=A[k]:
                num+=1
print(num)
