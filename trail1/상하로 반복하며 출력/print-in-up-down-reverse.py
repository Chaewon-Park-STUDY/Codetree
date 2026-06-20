
N= int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]


for i in range(N):
        for j in range(N):
            if j%2==0:
                arr[i][j]=i+1
            else:
                arr[i][j]=N-i

for elem in arr:
    for i in elem:
        print(i,end="")
    print()