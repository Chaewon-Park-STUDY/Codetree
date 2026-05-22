
store=[]

for i in range(10):
    store.append(int(input()))


count=0
for num in store:
    if num%2!=0:
        count+=1
    result= count
print(count)
