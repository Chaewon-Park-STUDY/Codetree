


cnt= []
for i in range(0,5):
    cnt.append(int(input()))

how_many=0

for num in cnt:
    if num%2==0:
        how_many+=1
print(how_many)