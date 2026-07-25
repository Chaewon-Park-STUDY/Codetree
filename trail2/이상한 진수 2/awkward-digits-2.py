a = input()

# Please write your code here.
arr=[]
for elem in a:
    arr.append(int(elem))


def binary(i):
    if arr[i]==1:
        return 1
    else:
        return 0

def check(n):
    num=0
    for i in range(len(n)):
        num= num*2+binary(i)
    return num
store=[]


if int(a)!=1:
    for i in range(1,len(arr)):
        if arr[i]==0:
            arr[i]=1
        else:
            arr[i]=0
        store.append(check(arr))
        if arr[i]==0:
            arr[i]=1
        else:
            arr[i]=0
    print(max(store))
else:
    print(0)