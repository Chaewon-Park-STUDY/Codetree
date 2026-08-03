arr=[int(input()) for _ in range(10)]

num_3=0
num_5=0

for elem in arr:
    if elem%3==0:
        num_3+=1
    if elem%5==0:
        num_5+=1

print(num_3, num_5, end=" ")