

arr=[list(map(int, input().split())) for _ in range(4)]


num=0

for elem in arr:
    for _ in elem:
        if _%5==0:
            num+=1
print(num)