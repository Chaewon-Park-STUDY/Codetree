n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

new=[]
max_value=0
for i in range(n-k+1):
    sum_value=0
    for j in range(i,i+k):
        sum_value+=arr[j]
    new.append(sum_value)
print(max(new))

