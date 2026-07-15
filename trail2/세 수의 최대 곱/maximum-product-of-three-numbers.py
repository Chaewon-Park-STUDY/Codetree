n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
num1=1
num2=arr[-1]

for elem in arr[-1:-4:-1]:
    num1*=elem
for elem in arr[:2]:
    num2*=elem
print(max(num1,num2))