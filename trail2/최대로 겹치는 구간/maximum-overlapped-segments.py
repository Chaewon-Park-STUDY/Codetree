n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


# Please write your code here.
arr=[]
new=[0 for _ in range(200)]
num=0
if any(elem[0]<0 for elem in segments):
    for elem in segments:
        if elem[0]<num:
            num=elem[0]
    for elem in segments:
        arr.append((elem[0]+abs(num),(elem[1]+abs(num))))

find=0
if len(arr)!=0:
    for elem in arr:
        for _ in range(elem[0],elem[1]):
            new[_]+=1
    for elem in new:
        if elem==max(new):
            find+=1
    if find==1:
        print(max(new))
    else:
         print(max(new))
else:
    for elem in segments:
        for _ in range(elem[0], elem[1]):
            new[_]+=1
    for elem in new:
        if elem==max(new):
            find+=1
    if find==1:
        print(max(new))
    else:
        print(max(new))