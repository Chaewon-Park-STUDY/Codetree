x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

def nonintersection(a,b,c,d):
    if b<c or d<a:
        return True
    else:
        return False

if nonintersection(x1,x2,x3,x4):
    print("nonintersecting")
else:
    print("intersecting")