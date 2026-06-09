arr=list(input())

for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break
for elem in arr:
    print(elem,end="")
