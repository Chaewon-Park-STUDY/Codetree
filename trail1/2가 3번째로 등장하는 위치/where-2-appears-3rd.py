N= int(input())

arr= list(map(int, input().split()))

num=0

for i in range(N):
    if arr[i] == 2:
        num+=1
        if num==3:
            print(i+1)
