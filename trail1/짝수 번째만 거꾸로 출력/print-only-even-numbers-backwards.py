arr=input()
new=[]

for i in range(1,len(arr),2):
    new.append(arr[i])


for i in range(len(new)-1,-1,-1):
    print(new[i],end="")