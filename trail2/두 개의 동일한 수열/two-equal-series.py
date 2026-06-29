n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

new_A= sorted(A)
new_B= sorted(B)

if new_A==new_B:
    print("Yes")
else:
    print("No")