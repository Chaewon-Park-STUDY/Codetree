arr=list(input())

new=[]

for elem in arr:
    if elem==arr[0]:
        elem= arr[1]
    elif elem==arr[1]:
        elem= arr[0]
    new.append(elem)


for _ in new:
    print(_, end="")