arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
a=arr[0]
b=arr[1]
c=arr[2]
d= max(arr)-a-b-c

def check(arr1,arr2):
    if len(arr1)!=len(arr2):
        return Fasle
    arr1.sort()
    arr2.sort()

    for x,y in zip(arr1,arr2):
        if x!=y:
            return False
    return True

print(a,b,c,d)