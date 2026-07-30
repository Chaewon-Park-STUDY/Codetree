n = int(input())
arr = list(input().split())

# Please write your code here.

for i in range(n):
    arr[i]= ord(arr[i])


num=0

for i in range(65,65+n):
    while arr[i-65]!=i:
        for j in range(n):
            new=arr.copy()
            if arr[j]==i:
                    if i-j>65: #오른쪽 가기
                        arr[j]=new[j+1]
                        arr[j+1]=i
                        num+=1
                    elif i-j<65:
                        arr[j]=new[j-1]
                        arr[j-1]=i
                        num+=1
print(num)