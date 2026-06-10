arr= input().split()

result= int(arr[0])+ int(arr[1])
num=0

for elem in str(result):
    if elem=="1":
        num+=1
print(num)