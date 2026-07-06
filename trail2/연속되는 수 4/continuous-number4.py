n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt=0
new=[]
# 1 5 2 3 5 8 8
# 0 1 2 3 4 5 6 
# 1 2 1 2 3 4 1
for i in range(n):
    if i==0 or arr[i-1]<arr[i]:
        cnt+=1
        if i==n-1:
            new.append(cnt)
    else:
        new.append(cnt)
        cnt=1
        if i==n-1:
            new.append(cnt)
print(max(new))

