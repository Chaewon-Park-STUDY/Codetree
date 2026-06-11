N= int(input())

for i in range(N):
    for j in range(0,i+1):
        print("*", end= " ")
    print()
for i in range(N-1):
    for j in range(0, N-i-1):
        print("*", end= " ")
    print()