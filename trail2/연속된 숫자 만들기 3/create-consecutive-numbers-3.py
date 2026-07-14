a = list(map(int, input().split()))

# Please write your code here.

if a[1]-a[0]==1 and a[2]-a[1]==1:
    print(0)
elif a[1]-a[0]==1:
    if a[2]-a[1]>2:
        print(a[2]-a[1]-1)
    else:
        print(1)
elif a[2]-a[1]==1:
    if a[1]-a[0]>2:
        print(a[1]-a[0]-1)
    else:
        print(1)
else:
    if a[1]-a[0]>a[2]-a[1]:
        print(a[1]-a[0]-1)
    else:
        print(a[2]-a[1]-1)