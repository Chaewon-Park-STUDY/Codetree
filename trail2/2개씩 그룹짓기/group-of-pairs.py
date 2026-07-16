n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

# 각 그룹의 원소합을 나열 했을 때 최댓값이 최대한 작아지도록 함 
# 2 3 5 5 n=2  0 2 3 5 5 1 4 2 3  for i in range(1,n+1):
# i+ (2n+1-i)

# 1 2 3 5 7 8  # 0 1 2 3 5 7 8 
# 1과 6 2 3 for i in range(1,n+1): i+ (2n+1-i)
#리스트에 append하고 max값 반환

nums.append(0)
nums.sort()

store=[]

for i in range(1,n+1):
    store.append(nums[i]+nums[2*n+1-i])
print(max(store))


