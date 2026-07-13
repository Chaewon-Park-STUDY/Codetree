n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.

def notintersect(a,b,c,d):
    if b<c or d<a:
        return True

store=[]
for i in range(n):
    num=0
    for j in range(n):
        if j!=i:
            for k in range(n):
                if k!=i and k!=j:
                    if not notintersect(x1[j],x2[j],x1[k],x2[k]):
                        num+=1
    store.append(num)

if any(elem==(n-2)*(n-1) for elem in store):
    print("Yes")
else:
    print("No")