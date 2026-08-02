
N= int(input())

sum_val=0
a=0
count=0
while sum_val<N:
    if sum_val>=N:
        break
    a+=1
    sum_val+=a
    count+=1
print(count)