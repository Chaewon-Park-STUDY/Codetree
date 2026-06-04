arr=[]
for i in range(10):
    arr.append(int(input()))

find=[]
for elem in arr:
    if 0<=elem<=200:
        find.append(elem)
result= sum(find)

print(result, round(result/len(find), 1), end= " ")


