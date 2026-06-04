arr_2d=[
    [0 for _ in range(5)]
    for _ in range(5)
]


for i in range(5):
    arr_2d[0][i] = 1
    arr_2d[i][0]=1


for i in range(1,5):
    num= arr_2d[i-1][0]
    for j in range(1,5):
        num+=arr_2d[i-1][j]
        arr_2d[i][j]= num


for row in arr_2d:
    for elem in row:
        print(elem, end= " ")
    print()