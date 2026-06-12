N= int(input())

for i in range(N):
    for j in range(N-i):
        print("*",end="")
    for k in range(i):
        print(""*2*i, end="  ")
    for m in range(N-i):
        print("*",end="")

    print()