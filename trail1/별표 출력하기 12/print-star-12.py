
N= int(input())


arr=[
    [" " for _ in range(N)]
    for _ in range(N)
]

for i in range(N):
    if i%2==0:
        arr[0][i]="*"
    else:
        for j in range(i+1):
            arr[j][i]="*"


for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()
