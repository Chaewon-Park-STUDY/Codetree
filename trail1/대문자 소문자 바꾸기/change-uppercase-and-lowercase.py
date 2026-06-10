arr=input()
new=[]

for elem in arr:
    if "A"<= elem<="Z":
        new.append(elem.lower())
    else:
        new.append(elem.upper())

for _ in new:
    print(_, end="")