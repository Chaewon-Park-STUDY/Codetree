N= int(input())
arr=[]

for i in range(N):
    arr.append(int(input()))

find=[]
for elem in arr:
    find.append(elem)
result= sum(find)

print(result, round(result/len(find),1), end= " ")