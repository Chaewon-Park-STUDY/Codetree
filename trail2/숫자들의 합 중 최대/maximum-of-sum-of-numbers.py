X, Y = map(int, input().split())

# Please write your code here.

new=[]
for i in range(X,Y+1):
    n=i
    store=0
    if n<10:
        new.append(n)

    while n//10>=0:
        store+=n%10
        n//=10
        if n==0:
            new.append(store)  
            break 

print(max(new))

