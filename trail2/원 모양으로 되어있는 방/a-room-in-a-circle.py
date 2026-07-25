n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.


def check(i,j):
    if i+j>n-1:
        return a[i+j-n]
    else:
        return False

min_value=10**9
for i in range(n):
    sum_total=0
    for j in range(1,n):
        if check(i,j)==False:
            sum_total+=j*a[i+j]
        else:
            sum_total+=j*check(i,j)
    min_value= min(min_value,sum_total)
print(min_value)
    


