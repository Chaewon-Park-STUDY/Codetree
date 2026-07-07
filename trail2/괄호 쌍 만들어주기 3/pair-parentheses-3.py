A = input()

# Please write your code here.
arr=[]
for elem in A:
    arr.append(elem)

n= len(A)
num=0
for i in range(n):
    if arr[i]=="(":
        for j in range(i+1,n):
            if arr[j]==")":
                num+=1
print(num)

