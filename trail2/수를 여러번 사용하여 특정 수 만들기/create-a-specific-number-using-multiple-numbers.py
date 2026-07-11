A, B, C = map(int, input().split())

# Please write your code here.

store=[]
for i in range(1000):
    num=A*i
    for j in range(1000):
        num=A*i
        num+=B*j
        if num<=C:
            store.append(num)
print(max(store))