arr= [input().split() for _ in range(3)]

store=[]
for elem in arr:
    if elem[0]=="Y":
        if int(elem[1])>=37:
            store.append("A")
        else:
            store.append("C")
    else:
        if int(elem[1])>=37:
            store.append("B")
        else:
            store.append("D")

if store.count("A")>=2:
    print("E")
else:
    print("N")