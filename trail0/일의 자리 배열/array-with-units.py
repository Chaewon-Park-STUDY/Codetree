
arr=list(map(int, input().split()))

new=[]
for i in range(10):
    if i==0 or i==1:
        print(arr[i], end=" ")
        new.append(arr[i])
    else:
        print((new[i-1]+new[i-2])%10, end=" ")
        new.append((new[i-1]+new[i-2])%10)