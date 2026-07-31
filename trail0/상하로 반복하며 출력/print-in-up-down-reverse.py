 
N= int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(N):
    for j in range(N):
        if i%2==0:
            arr[j][i]=j+1
        else:
            arr[j][i]=N-j

for elem in arr:
    for _ in elem:
        print(_,end="")
    print()