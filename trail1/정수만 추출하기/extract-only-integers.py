arr= input().split()
num1=''
num2=''


for elem in arr[0]:
    if elem.isdigit()==True:
        num1+=elem
    else:
        break

for elem in arr[1]:
    if elem.isdigit()==True:
        num2+=elem
    else:
        break
print(int(num1)+int(num2))
