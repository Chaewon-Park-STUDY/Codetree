arr=[list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j]*=3

for elem in arr:
    for _ in elem:
        print(_, end=" ")
    print()