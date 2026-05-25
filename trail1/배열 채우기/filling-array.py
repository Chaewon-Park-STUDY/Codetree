store=list(map(int, input().split()))
my=[]

for i in store:
    if i==0:
        break

    else:
        my.append(i)

for num in range(len(my)-1,-1,-1):
    print((my[num]), end= " ")
