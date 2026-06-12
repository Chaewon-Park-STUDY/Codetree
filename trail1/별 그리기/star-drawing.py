n = int(input())

# Please write your code here.
for i in range(n):
    for j in range(n-1-i):
        print("", end=" ")
    for k in range(2*i+1):
        print("*", end="")
    print()

for i in range(n-1):
    for j in range(i+1):
        print("", end= " ")
    for k in range(2*(n-2-i)+1):
        print("*", end="")
    print()