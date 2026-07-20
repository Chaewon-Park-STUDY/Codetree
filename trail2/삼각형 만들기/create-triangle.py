n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

x_pass=0
y_pass=0

for elem in x:
    if x.count(elem)>1:
        x_pass+=1
for elem in y:
    if y.count(elem)>1:
        y_pass+=1

max_wid=0
area=0
max_len=0
if x_pass>0 and y_pass>0:
    for i in range(n):
        wid=0
        length=0
        for j in range(n):
            if j!=i and x[i]==x[j]:
                wid= abs(y[i]-y[j])
                for k in range(n):
                    if k!=i and k!=j and y[k]==y[j]:
                        length= abs(x[k]-x[j])
                    elif k!=i and k!=j and y[k]==y[i]:
                        length= abs(x[k]-x[i])
                    area= max(area,wid*length)
            elif j!=i and y[i]==y[j]:
                length= abs(x[i]-x[j])
                for l in range(n):
                    if l!=i and l!=j and x[l]==x[j]:
                        wid= abs(y[l]-y[j])
                    elif l!=i and l!=j and x[l]==x[i]:
                        wid= abs(y[l]-y[i])
                    area= max(area,wid*length)

    print(area)
else:
    print(0)