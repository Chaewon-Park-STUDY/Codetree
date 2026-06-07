arr=[]

for i in range(5):
    arr.append(int(input()))

if all(x%3==0 for x in arr):
    print(1)
else:
    print(0)