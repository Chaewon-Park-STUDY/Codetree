n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
store=[]
max=0

for elem in nums:
    if nums.count(elem)==1:
        store.append(elem)
for num in store:
    if num>=max:
        max= num
if max>0:
    print(max)


if all(nums.count(x)>1 for x in nums):
    print(-1)