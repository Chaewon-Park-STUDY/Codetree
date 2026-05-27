
store= list(map(int, input().split()))

cnt=0
multiple_3=[]

for num in range(0,10):
    if num%2!=0:
        cnt+=store[num]
    if (num+1)%3==0:
        multiple_3.append(store[num])

avg= sum(multiple_3)/len(multiple_3)
print(cnt,round(avg,1), end= " ")


