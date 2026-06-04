A, B= map(int, input().split())

arr=[]


for i in range(A,B+1):
    if i%5==0 or i%7==0:
        arr.append(i)

print(sum(arr), round(sum(arr)/len(arr),1), end= " " )