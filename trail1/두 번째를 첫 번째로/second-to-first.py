arr=list(input())
new=[]
for elem in arr:
    if elem == arr[1]:
        elem= arr[0]
    new.append(elem)

for i in new:
    print(i,end="")
