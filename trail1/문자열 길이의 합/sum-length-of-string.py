N= int(input())

num=0
arr=[]
first=0

for j in range(N):
    arr.append(input())



for elem in arr:
    num+=len(elem)
    if elem[0]=="a":
        first+=1


print(num, first, end= " ")
