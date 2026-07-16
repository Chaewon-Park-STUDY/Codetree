arr = list(map(int, input().split()))

# Please write your code here.
# A가 최솟값, A+B+C가 최댓값
a=min(arr)

def check(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    arr1.sort()
    arr2.sort()

    for x,y in zip(arr1,arr2):
        if x!=y:
            return False
    return True
 
arr.sort()
b=arr[1]
for elem in arr:
    if elem>=b:
        c=elem
        if check([a,b,c,a+b,b+c,c+a,a+b+c],arr):
            print(a,b,c)
            break