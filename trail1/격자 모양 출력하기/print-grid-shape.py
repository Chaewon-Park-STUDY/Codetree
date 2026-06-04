N, M= map(int, input().split())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(M):
    r,c= tuple(map(int, input().split()))
    arr[r-1][c-1]= r*c

for row in arr:
    for elem in row:
        print(elem, end= " ")
    print()