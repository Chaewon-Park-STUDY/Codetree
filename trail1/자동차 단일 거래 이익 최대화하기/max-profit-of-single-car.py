n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

store=[]
for i in range(len(price)):
    for _ in range(i+1,len(price)):
        store.append(price[_]- price[i])

max=0

for elem in store:
    if elem>= max:
        max= elem
if max> 0:
    print(max)


if all (num<=0  for num in store):
    print(0)
