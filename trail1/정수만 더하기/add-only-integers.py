arr= input()
num=0

for elem in arr:
    if elem.isdigit()==True:
        num+=int(elem)
print(num)
