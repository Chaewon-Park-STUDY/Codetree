N= int(input())

arr_2d=[
    [0 for _ in range(N)]
    for _ in range(N)
]


for i in range(N-1, -1, -2):
    num= 1+ N*(N-1-i)
    for j in range(0,N):
        arr_2d[N-1-j][i]= num
        num+=1

for i in range(N-2,-1,-2):
    digit=(N+1) + N*(N-2-i)
    for j in range(0, N):
        arr_2d[j][i]= digit
        digit+=1


for row in arr_2d:
    for elem in row:
        print(elem, end= " ")
    print()