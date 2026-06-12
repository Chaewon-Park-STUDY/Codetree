N= int(input())

for i in range(N):
    for j in range(i):
        print(" ", end= " ")
    for k in range(2*(N-i)-1):
        print("*", end= " ")
    print()

for i in range(N-1):
    for j in range(N-i-2):
        print(" ", end= " ")
    for k in range(2*(i+1)+1):
        print("*", end= " ")
    print()