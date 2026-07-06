N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
# 2 -1 -5 -2 -3 5 8
# 0  1  2  3  4 5 6

cnt=0
new=[]
for i in range(N):
    if i==0 or arr[i]*arr[i-1]<0:
        cnt+=1
        if i==N-1:
            new.append(cnt)
        else:
            if arr[i]*arr[i+1]>0:
                cnt+=1
            else:
                new.append(cnt)
                cnt=0
    else:
        if i==N-1:
            new.append(cnt)
        else:
            if arr[i]*arr[i+1]>0:
                cnt+=1
            else:
                new.append(cnt)
                cnt=0
print(max(new))
  