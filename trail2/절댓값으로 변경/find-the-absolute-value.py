n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def logic(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

logic(arr)
for elem in arr:
    print(elem, end=" ")