n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

new=[]
for i in range(n-2):
    for j in range(i+2,n):
        new.append(numbers[i]+numbers[j])
print(max(new))
