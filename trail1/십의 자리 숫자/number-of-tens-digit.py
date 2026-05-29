
arr= list(map(int, input().split()))

store=[]
for num in arr:
    if num!=0:
        store.append(num//10)
    else:
        break

for i in range(1,10):
    print(f"{i} - {store.count(i)}")
