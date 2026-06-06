arr=["apple", "banana", "grape", "blueberry", "orange"]
new=[]
num=0

N= input()

for elem in arr:
    if elem[2]==N or elem[3]==N:
        new.append(elem)
        num+=1
for i in new:
    print(i)
print(num)
