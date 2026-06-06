arr=[]
length=[]

for i in range(3):
    arr.append(input())

for elem in arr:
    length.append(len(elem))

min=20
max=0

for i in length:
    if i>=max:
        max=i
    if i<=min:
        min=i
print(max-min)