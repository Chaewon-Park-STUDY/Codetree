a, b, c = map(int, input().split())

# Please write your code here.
h,t,m= (11,11,11)

time=0
while True:
    if a==11 and b<11:
        time=-1
        break
    if a==11 and b==11 and c<11:
        time=-1
        break

    if h==a and t==b and m==c:
        break

    time+=1
    m+=1

    if m==60:
        t+=1
        m=0
        if t==24:
            h+=1
            t=0
print(time)
    