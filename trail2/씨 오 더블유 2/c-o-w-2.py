n = int(input())
S = input()

# Please write your code here.
arr=[]
for elem in S:
    arr.append(elem)

new=[]
for i in range(n-2):
    if arr[i]=="C":
        for j in range(i+1,n-1):
            if arr[j]=="O":
                for k in range(j+1,n):
                    if arr[k]=="W":
                        new.append((i,j,k))
print(len(new))