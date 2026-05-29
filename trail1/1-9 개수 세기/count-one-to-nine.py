
N= int(input())

arr= list(map(int, input().split()))


for i in range(1,10):
    if i in arr:
        print(arr.count(i))
    else:
        print(0)