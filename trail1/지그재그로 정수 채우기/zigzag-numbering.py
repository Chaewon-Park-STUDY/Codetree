n, m = map(int, input().split())

# Please write your code here.
arr_2d=[
    [0 for _ in range(m)]
    for _ in range(n)
]



for i in range(0,m,2):
    num= n*i
    for j in range(0,n):
        arr_2d[j][i]= num
        num+=1


for i in range(1,m,2):
    digit= n*i
    for j in range(n-1,-1,-1):
        arr_2d[j][i]= digit
        digit+=1


for row in arr_2d:
    for elem in row:
        print(elem, end= " ")
    print()


