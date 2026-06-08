arr=input()
num_1=0
num_2=0


for i in range(len(arr)-1):
    if arr[i]=="e" and arr[i+1]=="e":
        num_1+=1

for j in range(len(arr)-1):
    if arr[j]=="e" and arr[j+1]=="b":
        num_2+=1
print(num_1, num_2, end= " ")