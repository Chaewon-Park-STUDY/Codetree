n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

def notintersect(a,b,c,d):
    if b<c or d<a:
        return True

num=0

for i in range(n):
    for j in range(i+1,n):
        if not notintersect(x1[i],x2[i],x1[j],x2[j]):
            num+=1
if num==(n-1)*n//2:
    print("Yes")
else:
    print("No")
