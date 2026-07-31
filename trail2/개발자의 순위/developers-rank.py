k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.

num=0

for i in range(1,n+1):
    for j in range(1,n+1):
        total=0
        if j!=i:
            for elem in arr:
                if elem.index(i)>elem.index(j):
                    total+=1
                    continue

                else:
                    break
            if total==k:
                num+=1
print(num)