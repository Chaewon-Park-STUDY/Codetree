X, Y = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(X,Y+1):
    new=[]
    first=0
    second=0
    arr=list(map(int, list(str(i))))
    n= len(arr)
    for elem in arr:
        if elem not in new:
            new.append(elem)
    if len(new)==2:
        for elem in arr:
            if elem==new[0]:
                first+=1
            else:
                second+=1
        if abs(first-second)==n-2:
            cnt+=1
print(cnt)

