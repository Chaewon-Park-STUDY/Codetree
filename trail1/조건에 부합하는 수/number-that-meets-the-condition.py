A= int(input())
arr=[]

for i in range(1, A+1):
    if i%2==0 and i%4!=0:
        pass
    elif (i//8)%2==0:
        pass
    elif i%7<4:
        pass
    else:
        arr.append(i)

for elem in arr:
    print(elem, end= " ")