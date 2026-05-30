
arr= list(map(int, input().split()))
store= list(map(int, input().split()))
N= arr[0]
M= arr[1]

num=0
for elem in store:
    if elem== M:
        num+=1

print(num)
