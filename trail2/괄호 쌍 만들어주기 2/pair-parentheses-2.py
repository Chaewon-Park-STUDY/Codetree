A = input()

# Please write your code here.
arr=[]

for elem in A:
    arr.append(elem)

n= len(arr)
new=[]
num=0



on=True
while on:
    for i in range(n-3):
        if arr[i]=="(" and arr[i+1]=="(":
                for k in range(i+2,n-1):
                    if arr[k]==")" and arr[k+1]==")":
                        new.append((i,k))
                        on=False
print(len(new))


