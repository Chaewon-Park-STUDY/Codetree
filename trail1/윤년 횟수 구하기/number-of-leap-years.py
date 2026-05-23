
N= int(input())

num=0
for day in range(1, N+1):
    if day%4==0:
        if day%100==0 and day%400!=0:
            num+=0
        else:
            num+=1
print(num)
