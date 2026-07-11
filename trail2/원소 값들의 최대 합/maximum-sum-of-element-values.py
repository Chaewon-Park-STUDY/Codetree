n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

max_value=0
for i in range(1,n+1):
    sum_val=0
    new=arr[i]
    for j in range(m): 
        sum_val+=new
        new=arr[new]
    max_value= max(max_value,sum_val)

print(max_value)