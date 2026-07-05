N = input()

# Please write your code here.
num=0
arr=[]
for elem in N:
    arr.append(int(elem))

for i in range(len(N)):
    num= num*2+ arr[i]

num*=17
new=[]
while True:
    if num<2:
        new.append(num)
        break
    new.append(num%2)
    num//=2

for elem in new[::-1]:
    print(elem,end="")
