x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

#arr 배열에서 0이 아닌 1로 남아있는 숫자는 1이 써 있는 max좌표 5x 1이 써 ㅣ쓴 max-min좌표 곱하기

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

a=min(x)
b=min(y)

if a<0:
    for i in range(2):
        x1[i]+=-a
        x2[i]+=-a
if b<0:
    for i in range(2):
        y1[i]+=-b
        y2[i]+=-b

wid= max(x2)-min(x1)
length= max(y2)-min(y1)

arr=[
    [0 for _ in range(length)]
    for _ in range(wid)
]

for i in range(2):
    for j in range(x1[i]-min(x1),x2[i]-min(x1)):
        for k in range(y1[i]-min(y1),y2[i]-min(y1)):
            if i!=1:
                arr[j][k]+=1
            else:
                arr[j][k]-=1


max_x=0
min_x=10**6
max_y=0
min_y=10**6


if x2[1]>=x2[0] and x1[1]<=x1[0] and y2[1]>=y2[0] and y1[1]<=y1[0]:
    print(0)
else:
    for i in range(wid):
        for j in range(length):
            if arr[i][j]>0:
                max_x= max(max_x,i)
                min_x= min(min_x,i)
                max_y= max(max_y,j)
                min_y= min(min_y,j)
    print((max_x-min_x+1)*(max_y-min_y+1))
