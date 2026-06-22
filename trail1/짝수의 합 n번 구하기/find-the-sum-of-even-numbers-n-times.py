N= int(input())

arr=[]

for i in range(N):
    arr.append(list(map(int, input().split())))


for elem in arr:
    num=0
    for i in range(elem[0], elem[1]+1):
        if i%2==0:
            num+=i
    print(num)
