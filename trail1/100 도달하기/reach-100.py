
N= int(input())

store= []
store.append(1)
store.append(N)


for i in range(100):
    if store[i+1]<100:
        store.append(store[i]+store[i+1])
    else:
        for num in store:
            print(num, end= " ")
        break