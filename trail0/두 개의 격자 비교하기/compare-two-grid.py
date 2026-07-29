
N, M= list(map(int, input().split()))

arr1=[list(map(int, input().split()))for _ in range(N)]
arr2=[list(map(int, input().split()))for _ in range(N)]

new=[
    [0 for _ in range(M)]
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        if arr1[i][j]==arr2[i][j]:
            new[i][j]=0
        else:
            new[i][j]=1

for elem in new:
    for _ in elem:
        print(_, end=" ")
    print()