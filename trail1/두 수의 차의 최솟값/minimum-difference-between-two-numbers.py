N= int(input())

arr= list(map(int, input().split()))

store=[]


for i in range(len(arr)):
    for _ in range(i+1,len(arr)):
        store.append(abs(arr[i]-arr[_]))

min= 99

for num in store:
    if num<=min:
        min=num
print(min)