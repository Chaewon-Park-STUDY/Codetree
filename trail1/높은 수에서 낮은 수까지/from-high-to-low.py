
A, B= map(int, input().split())

big= max(A,B)
small= min(A,B)

for num in range(big, small-1, -1):
    print(num, end=" ")