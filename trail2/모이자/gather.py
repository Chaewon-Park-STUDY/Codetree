n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

new=[]
for i in range(n):
    max_value=0
    sum_value=0
    for j in range(n):
        sum_value+=abs((j-i)*A[j])
    if sum_value>max_value:
        max_value= sum_value
    new.append(max_value)
print(min(new))

