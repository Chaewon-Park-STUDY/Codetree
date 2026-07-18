n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
store=[]


for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            store.append((arr[i],arr[j],arr[k]))

new=[]

for x,y,z in store:
    num=0
    for i in range(5):
        if (x//10**i)%10 + (y//10**i)%10 + (z//10**i)%10<10:
            num+=1
    if num==5:
        new.append(x+y+z)


if len(new)!=0:
    print(max(new))
else:
    print(-1)


