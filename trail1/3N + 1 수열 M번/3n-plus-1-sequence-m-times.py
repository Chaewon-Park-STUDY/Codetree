N= int(input())
arr=[]

for i in range(N):
    arr.append(int(input()))



for elem in arr:
    num=0
    while elem!=1:
        if elem%2==0:
            elem=elem/2
            num+=1
        else:
            elem=elem*3+1
            num+=1
    print(num)