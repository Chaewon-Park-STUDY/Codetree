N= int(input())

arr=[]
for i in range(1, N+1):
    if i%2!=0:
        if i%5!=0:
            if i%3==0 and i%9!=0:
                pass
            else:
                arr.append(i)


for elem in arr:
    print(elem, end= " ")
