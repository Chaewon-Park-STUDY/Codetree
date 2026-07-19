N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

total=0
arr=[]
for k in range(N-M+1):
    arr.append(B.copy())

for i in range(N-M+1):
    num=0
    for j in range(i,i+M):
        for m in range(len(B)):
            if A[j]==B[m]:
                B.pop(m)
                break
    if len(B)==0:
        total+=1
    B=arr[i]

print(total)