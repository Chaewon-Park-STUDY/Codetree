N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

# 1 6 4 3 1 max-min <=3 되도록
# 최솟값을 a라고 했을 때 
# [a,a+3]내에서 선택
# a의 범위는?
# a는 arr에 있는 원소들 중 하나씩 선택
max_val=0
for i in range(N):
    num=1
    for j in range(N):
        if i!=j:
            if arr[i]<=arr[j]<=arr[i]+K:
                num+=1
    max_val= max(max_val,num)
print(max_val)

