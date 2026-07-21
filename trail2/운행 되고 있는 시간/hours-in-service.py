n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
#아하 겹치는 시간 제외!


def is_intersect(a,b,c,d): #a,b가 한 쌍 c,d가 다른 한 쌍
    if c<=a and b<=d:
        return -(b-a)
    elif c<=a and a<=d<=b:
        return -(d-a)
    elif a<=c<=b and b<=d:
        return -(b-c)
    elif a<=c and d<=b:
        return -(d-c)
    else:
        return False


max_value=0
for i in range(n):
    total=0
    num=0
    for j in range(n):
        if num==n-1:
            break
        if j!=i:
            num+=1
            total+=b[j]-a[j]
            for k in range(j+1,n):
                if k!=i:
                    if is_intersect(a[j],b[j],a[k],b[k])==False:
                        pass
                    else:
                        total+=is_intersect(a[j],b[j],a[k],b[k])
    max_value= max(max_value,total)

print(max_value)