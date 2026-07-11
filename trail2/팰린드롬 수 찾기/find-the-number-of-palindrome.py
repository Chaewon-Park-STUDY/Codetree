X, Y = map(int, input().split())

# Please write your code here.

cnt=0
for i in range(X,Y+1):
    new= list(map(int, list(str(i))))
    if new[::]==new[::-1]:
        cnt+=1
print(cnt)