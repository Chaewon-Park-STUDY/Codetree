n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min=2^31-1
num=0

for i in range(1,n):
    if a[i-1] >= a[i]:
        min= a[i]

for elem in a:
    if min<= elem:
        pass
    else:
        min= elem

for cnt in a:
    if cnt==min:
        num+=1

print(min, num, end= " ")