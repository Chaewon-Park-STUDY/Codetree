n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
i=0
def calculation(n):
    global i
    if n==0:
        return 
    if i<arr[n-1]:
        i= arr[n-1]
    calculation(n-1)
    return i

print(calculation(n))