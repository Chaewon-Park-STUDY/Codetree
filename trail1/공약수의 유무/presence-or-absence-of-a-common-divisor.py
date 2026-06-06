A,B= map(int, input().split())

arr=[]

for i in range(A, B+1):
    if 1920%i==0 and 2880%i==0:
        arr.append(i)
    else:
        pass
if len(arr)>0:
    print(1)
else:
    print(0)