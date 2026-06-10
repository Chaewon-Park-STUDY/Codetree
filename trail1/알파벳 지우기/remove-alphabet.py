num1=input()
num2=input()
new1=[]
new2=[]
result1=''
result2=''

for elem in num1:
    if elem.isdigit()==True:
        new1.append(elem)

for elem in num2:
    if elem.isdigit()==True:
        new2.append(elem)


for elem in new1:
    result1+=elem
for elem in new2:
    result2+=elem
print(int(result1)+ int(result2))
