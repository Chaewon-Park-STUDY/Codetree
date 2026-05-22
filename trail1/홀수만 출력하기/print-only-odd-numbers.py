
store=[]
N= int(input())

for num in range(N):
    store.append(int(input()))

for i in store:
    if i %3==0 and i%2!=0:
        print(i)
