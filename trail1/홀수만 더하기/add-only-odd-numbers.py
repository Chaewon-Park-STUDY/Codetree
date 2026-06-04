N= int(input())

num=0
arr=[]
for i in range(N):
    arr.append(int(input()))


for elem in arr:
    if elem%2!=0 and elem%3==0:
        num+=elem
print(num)
