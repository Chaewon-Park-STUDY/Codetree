N= int(input())

arr= input().split()
num=''
for elem in arr:
    num+=elem

m= len(num)//5 #4
n= len(num)%5#1

for i in range(m):
    for j in range(5*i,5*i+5):
        print(num[j],end="")
    print()

for _ in range(5*m, len(num)):
    print(num[_],end="")