arr=[]

for i in range(10):
    arr.append(input())


N= input()
new=[]

for elem in arr:
    if elem[-1]== N:
        new.append(elem)

if len(new)>0:
    for elem in new:
        print(elem)
else:
    print("None")