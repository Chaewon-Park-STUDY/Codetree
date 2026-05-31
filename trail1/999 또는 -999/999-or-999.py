arr= list(map(int, input().split()))
new=[]
max=-1000
min= 999

for i in range(len(arr)):
    if arr[i]== 999 or arr[i]==-999:
        new= arr[0:i]
        break
for num in new:
    if num>= max:
        max=num
for _ in new:
    if _<=min:
        min= _
print(max, min, end= " ")