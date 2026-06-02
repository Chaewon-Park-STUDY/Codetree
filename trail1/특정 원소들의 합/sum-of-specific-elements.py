sum_val=0
for _ in range(4):
    arr= list(map(int, input().split()))
    for j in range(0,_+1):
        sum_val+=arr[j]
print(sum_val)