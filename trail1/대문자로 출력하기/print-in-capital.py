arr=input()
new=[]

for elem in arr:
    if elem.isalpha()==True:
        new.append(elem.upper())

for elem in new:
    print(elem,end="")