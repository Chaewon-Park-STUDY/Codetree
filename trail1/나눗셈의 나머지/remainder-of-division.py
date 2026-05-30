arr= list(map(int, input().split()))
A = arr[0]
B= arr[1]
store=[]

is_on= True
while is_on:
    A/B
    store.append(A%B)
    A= A//B
    if A<=1:
        is_on= False


result=0
for i in range(10):
    if i in store:
        result += (store.count(i))**2
print(result)
    