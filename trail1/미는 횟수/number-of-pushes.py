A= input()
B= input()
arr=[]

for i in range(len(A)):
    A= A[-1] + A[0:-1]
    arr.append(A)
    A=A


for i in range(len(arr)):
    if arr[i] == B:
        print(i+1)
        break

if all(arr[i]!=B for i in range(len(arr))):
    print(-1)