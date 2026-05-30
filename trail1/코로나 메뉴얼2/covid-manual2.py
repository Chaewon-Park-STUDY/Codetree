
arr=[]
A=0
B=0
C=0
D=0

for _ in range(3):
    arr+=list(map(str, input().split()))


for i in range(0,5,2):
    if arr[i]=="Y":
        if int(arr[i+1])>=37:
            A+=1
        else:
            C+=1
    elif arr[i]== "N":
        if int(arr[i+1])>=37:
            B+=1
        else:
            D+=1

num=0

if A>=2:
    num+=1
emerg= ['E']


if A>=2:
    print(A,B,C,D,emerg[0], end= " ")
else:
    print(A,B, C, D, end= " ")