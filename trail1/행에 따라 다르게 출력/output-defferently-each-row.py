N= int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]



cnt=0
for i in range(N):
    if i%2==0:
        for j in range(N):
            cnt+=1
            arr[i][j]=cnt
    else:
        for j in range(N):
            cnt+=2
            arr[i][j]=cnt

for elem in arr:
    for i in elem:
        print(i, end=" ")
    print()