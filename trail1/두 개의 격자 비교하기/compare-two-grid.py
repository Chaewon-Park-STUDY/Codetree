N, M= map(int, input().split())

arr=[]
cnt=[]
for i in range(N):
    arr.append(list(map(int, input().split())))

for j in range(N):
    cnt.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if arr[i][j] == cnt[i][j]:
            print(0, end= " ")
        else:
            print(1, end= " ")
    print()
