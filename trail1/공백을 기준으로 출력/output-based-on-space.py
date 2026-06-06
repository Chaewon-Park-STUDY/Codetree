N= input()
N2= input()
arr=[]
for elem in N:
    if elem!=" ":
        arr.append(elem)
for i in N2:
    if i!=" ":
        arr.append(i)

for _ in arr:
    print(_, end="")
