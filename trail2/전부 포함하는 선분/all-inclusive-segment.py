n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
length=100
for i in range(n):
    store=[]
    min_val=100
    max_val=1
    for j in range(n):
        if j!=i:
            store.append(segments[j])
    for elem in store:
        min_val= min(min_val,elem[0])
        max_val= max(max_val, elem[1])
    length= min(length, max_val-min_val)


print(length)

