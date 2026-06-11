arr=[]

for i in range(10):
    elem=input()
    if elem!= "END":
        arr.append(elem)
    else:
        break

for elem in arr:
    print(elem[::-1])