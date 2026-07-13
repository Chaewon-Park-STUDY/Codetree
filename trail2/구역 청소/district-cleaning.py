a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

num= (b-a)+(d-c)
def intersect_check(a,b,c,d):
    global num
    if c<=a:
        if a<d<=b:
            num-=(d-a)
        elif d>b:
            num-=(b-a)
    elif a<c<b:
        if d<b:
            num-=(d-c)
        else:
            num-=(b-c)
    else:
        pass
    return num

print(intersect_check(a,b,c,d))