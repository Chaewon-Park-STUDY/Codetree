A, B= map(int, input().split())

sum_val=0
min=0
max=0

if A>=B:
    min,max=B,A
else:
    min, max= A, B

for i in range(min, max+1):
    if i%5==0:
        sum_val+=i
print(sum_val)