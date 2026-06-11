N= int(input())

for i in range(N):
    for j in range(N-i,0,-1):
        print("*", end= " ")
    print()

for i in range(N-1):
    for j in range(2+i):
        print("*", end= " ")
    print()