n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

new=[]
cnt=0

# 1 6 7 8 3 4 5
# 0 1 2 3 4 5 6

for i in range(n):
    if arr[i]>t:
        cnt+=1
        if i==n-1:
            new.append(cnt)
    else:
        new.append(cnt)
        cnt=0
print(max(new))