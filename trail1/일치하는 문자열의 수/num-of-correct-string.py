n, A= input().split()
arr=[]
num=0

for i in range(int(n)):
    arr.append(input())

for elem in arr:
    if elem== A:
        num+=1
print(num)