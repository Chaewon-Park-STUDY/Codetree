
N= int(input())

#약수를 어떻게 구할까?

arr=[]
for i in range(1, N):
    if N%i==0:
        arr.append(i)

if sum(arr)==N:
    print("P")
else:
    print("N")