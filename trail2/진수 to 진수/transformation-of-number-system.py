a, b = map(int, input().split())
n = input()

# Please write your code here.
arr=[]
new=[]

for elem in n:
    arr.append(int(elem))
num=0
for i in range(len(n)):
    num= num*a+arr[i]

while True:
    if num<b:
        new.append(num)
        break
    new.append(num%b)
    num//=b
for elem in new[::-1]:
    print(elem,end="")

