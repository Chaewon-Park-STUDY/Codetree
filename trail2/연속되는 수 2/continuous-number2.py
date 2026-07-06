n = int(input())
arr = [int(input()) for _ in range(n)]


# Please write your code here.
new=[]
cnt=0
for i in range(n):
    if i==0 or arr[i]!=arr[i-1]:
        cnt+=1
        if i==n-1:
            new.append(cnt)
            break
        if arr[i]==arr[i+1]:
            pass
        else:
            new.append(cnt)
            cnt=0
    else:
        cnt+=1
        if i==n-1:
            new.append(cnt)
            break
        if arr[i]!=arr[i+1]:
            new.append(cnt)
            cnt=0
 
print(max(new))

