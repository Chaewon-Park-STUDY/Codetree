N= int(input())

for i in range(N):
    for j in range(N-i):
        for k in range(N-i):
            print("*",end="")
        print(end=" ")
    print()