n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.



def intersection(a,b,c,d):
    if a<b:
        if a<c and d<b or c<a and d>b or d<c and d<b:
            return True
    elif a>b:
        if a<c and d<b or b<=c and b<d or c<b and b<d:
            return True
    elif a==b:
        if c<a and d>b or a<c and d<b:
            return True
    elif c==d:
        if a<c and b>d or c<a and b<d:
            return True

store=[]
for i in range(n-1):
    for j in range(i+1,n):
        if intersection(lines[i][0],lines[i][1],lines[j][0],lines[j][1])==True:
            if i not in store:
                store.append(i)
            if j not in store:
                store.append(j)

print(n-len(store))