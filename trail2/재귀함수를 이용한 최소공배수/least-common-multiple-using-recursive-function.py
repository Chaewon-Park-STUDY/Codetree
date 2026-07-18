n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
num=1


def division(a,b):
    if b==-1:
        return a
    for i in range(arr[b],0,-1):
        if a%i==0 and arr[b]%i==0:
            return division((a//i)*(arr[b]//i)*i,b-1)


print(division(num,n-1))

        