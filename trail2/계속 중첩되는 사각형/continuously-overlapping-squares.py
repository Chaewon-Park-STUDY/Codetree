n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

a=min(x1)
b= min(y1)

if a<0:
    for i in range(n):
        x1[i]+=-a
        x2[i]+=-a
if b<0:
    for i in range(n):
        y1[i]+=-b
        y2[i]+=-b

wid= max(x2)-min(x1)
length= max(y2)-min(y1)

col=[
    [0 for _ in range(length)]
    for _ in range(wid)
]


for i in range(n):
    for j in range(x1[i]-min(x1),x2[i]-min(x1)):
        for k in range(y1[i]-min(y1),y2[i]-min(y1)):
            if i%2==0:
                col[j][k]="R"
            else:
                col[j][k]="B"


num=0
for elem in col:
    for _ in elem:
        if _=="B":
            num+=1
print(num)
