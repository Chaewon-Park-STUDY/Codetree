num_3=0
num_5=0

store=[]

for num in range(10):
    store.append(int(input()))


for i in store:
    if i%3==0 and i%15!=0:
        num_3+=1
    elif i%5==0 and i%15!=0:
        num_5+=1
    elif i%15==0:
        num_3+=1
        num_5+=1
print(num_3, num_5, end= " ")
