n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

max_val=0


for i in range(m):
    num=0
    for j in range(m):
        if pairs[i][::]==pairs[j][::-1] or pairs[i][::]==pairs[j][::]:
            num+=1
    max_val=max(max_val,num)
print(max_val)