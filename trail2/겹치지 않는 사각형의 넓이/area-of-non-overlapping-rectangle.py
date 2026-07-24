x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
x=[]
y=[]

for elem in x1:
    x.append(elem)
for elem in x2:
    x.append(elem)
for elem in y1:
    y.append(elem)
for elem in y2:
    y.append(elem)

a= min(x)
b= min(y)

for i in range(3):
    if a<0:
        x1[i]+=-a
        x2[i]+=-a
    if b<0:
        y1[i]+=-b
        y2[i]+=-b

wid= max(x2)-min(x1)
len= max(y2)-min(y1)

arr=[
    [0 for _ in range(len)]
    for _ in range(wid)
]

for i in range(3):
    for j in range(x1[i]-min(x1),x2[i]-min(x1)):
        for k in range(y1[i]-min(y1),y2[i]-min(y1)):
            if i!=2:
                arr[j][k]+=1
            else:
                arr[j][k]-=1


num=0

for elem in arr:
    for _ in elem:
        if _>0:
            num+=1
print(num)
