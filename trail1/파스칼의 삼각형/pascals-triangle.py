N= int(input())
arr=[]
for i in range(1, N+1):
    arr.append([1 for _ in range(i)])


for i in range(2,N):
    for j in range(1,i):
        arr[i][j]=arr[i-1][j] + arr[i-1][j-1]

for row in arr:
    for elem in row:
        print(elem, end= " ")
    print()