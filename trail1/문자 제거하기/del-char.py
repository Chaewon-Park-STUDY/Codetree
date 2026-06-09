arr=list(input())
new=[]
for i in range(len(arr)-1):
    new.append(int(input()))


for elem in new:
    if elem<len(arr):
        arr.pop(elem)
        s=''.join(arr)
        print(s)
    else:
        arr.pop(-1)
        s=''.join(arr)
        print(s)

