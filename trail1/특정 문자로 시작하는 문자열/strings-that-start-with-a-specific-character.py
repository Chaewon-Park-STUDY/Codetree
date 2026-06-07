N= int(input())
arr=[]
num=0
long=[]

for i in range(N):
    arr.append(input())


alphabet= input()

for elem in arr:
    if elem[0]== alphabet:
        num+=1
        long.append(len(elem))

print(num, format(sum(long)/len(long),'.2f'), end= " " )

