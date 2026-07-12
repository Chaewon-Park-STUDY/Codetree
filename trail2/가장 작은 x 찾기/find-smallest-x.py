n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

new=[]
for i in range(1,10001):
    num=0
    for j in range(n):
        i*=2
        if a[j]<=i<=b[j]:
            num+=1
        if num==n:
            new.append(i//2**n)
print(min(new))
        
