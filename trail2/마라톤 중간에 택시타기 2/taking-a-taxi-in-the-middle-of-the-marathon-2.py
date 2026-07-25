n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
#new_X에 총 n-1개가, 즉 3개  담김 range(n-2)까지 

min_value=10**6
for i in range(1,n-1):
    num=0
    sum_diff=0
    new_x=[]
    new_y=[]
    new_x.append(x[0])
    new_y.append(y[0])
    for j in range(1,n-1):
        if j!=i:
            new_x.append(x[j])
            new_y.append(y[j])
    new_x.append(x[n-1])
    new_y.append(y[n-1])

    for k in range(n-2):
        sum_diff+=abs(new_x[k]-new_x[k+1])+abs(new_y[k]-new_y[k+1])
    min_value= min(min_value, sum_diff)
print(min_value)


