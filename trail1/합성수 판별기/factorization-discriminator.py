N= int(input())

arr=[]

for i in range(2, N):
    if N%i==0:
        arr.append(i)

if len(arr)>0:
    print("C")
else:
    print("N")