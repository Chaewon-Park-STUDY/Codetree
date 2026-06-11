arr=[]
num=0


for i in range(200):
    elem= input()
    if elem != "0":
        arr.append(elem)
        num+=1
    else:
        break

print(num)

for i in range(0,len(arr),2):
    print(arr[i])