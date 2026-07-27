
N= int(input())

arr=[list(map(int, input().split())) for _ in range(N)]


for _ in range(N):
    num=0
    for elem in range(arr[_][0],arr[_][1]+1):
        if elem%2==0:
            num+=elem
    print(num)
