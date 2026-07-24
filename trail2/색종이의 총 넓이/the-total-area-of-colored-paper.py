n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
a=min(x)
b= min(y)

if a<0:
    for i in range(n):
        x[i]+=-a
if b<0:
    for i in range(n):    
        y[i]+=-b
store_x=[]
store_y=[]

for elem in x:
    store_x.append(elem)
    store_x.append(elem+8)
for elem in y:
    store_y.append(elem)
    store_y.append(elem+8)

wid=max(store_x)-min(store_x)
length=max(store_y)-min(store_y)


arr=[
    [0 for _ in range(length)]
    for _ in range(wid)
]



for i in range(n):
    for j in range(x[i]-min(x),x[i]+8-min(x)):
        for k in range(y[i]-min(y),y[i]+8-min(y)):
            arr[j][k]+=1

num=0
for elem in arr:
    for _ in elem:
        if _!=0:
            num+=1
print(num)