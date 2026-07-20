n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

min_area=10**10
for i in range(n):
    wid=[]
    len=[]
    for j in range(n):
        if j!=i:
            wid.append(x[j])
            len.append(y[j])
    area= (max(wid)-min(wid))*(max(len)-min(len))
    min_area=min(min_area,area)
print(min_area)


