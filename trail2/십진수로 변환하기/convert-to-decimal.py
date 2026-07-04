binary = input()


# Please write your code here.
num=0
arr=[]
for elem in binary:
    arr.append(int(elem))

for i in range(len(binary)):
    num= num*2+ arr[i]
print(num)