arr=input()
new=[]

for elem in arr:
    if elem.isalpha() ==True:
        elem= elem.lower()
        new.append(elem)
    elif elem.isdigit()==True:
        new.append(elem)

for elem in new:
    print(elem,end="")