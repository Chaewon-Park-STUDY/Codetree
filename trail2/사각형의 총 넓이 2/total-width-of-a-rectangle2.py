n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
#arr를 만들고
# 해당 좌표 내 구역이면 1
# 이미 elem1 이면 채우지 않고 나머지 채우고 최종적으로 arr안에 있는 1의 개수를 셈=답

min_value= min(min(x1),min(y1),min(x2),min(y2))
if min_value<0:
    for i in range(n):
        x1[i]+=-min_value
        x2[i]+=-min_value
        y1[i]+=-min_value
        y2[i]+=-min_value
store=[max(y2),max(x2)]
new=max(store)


arr=[
    [0 for _ in range(new)]
    for _ in range(new)
]



for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            if arr[j][k]!=1:
                arr[j][k]=1
num=0
for elem in arr:
    for _ in elem:
        if _==1:
            num+=1
print(num)
