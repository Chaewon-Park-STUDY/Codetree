N= int(input())
arr=list(map(int, input().split()))

store=[]

for elem in arr:
    if elem%2==0:
        store.append(elem)
store.reverse()

for i in store:
    print(i, end=" ")