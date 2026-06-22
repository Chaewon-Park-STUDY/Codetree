N= int(input())

arr=[]

for i in range(1,N+1):
    num=0
    for j in range(1,i+1):
        if i%j==0:
            num+=1
    if num==2:
        arr.append(i)

for elem in arr:
    print(elem, end=" ")