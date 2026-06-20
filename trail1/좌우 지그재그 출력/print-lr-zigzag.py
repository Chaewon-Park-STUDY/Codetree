N= int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]

cnt=1
for i in range(N):
    if i%2==0:
        for j in range(N):
            arr[i][j]=cnt
            cnt+=1
    else:
        for j in range(N):
            arr[i][N-1-j]=cnt
            cnt+=1


for elem in arr:
    for i in elem:
        print(i, end=" ")
    print()