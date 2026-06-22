N= int(input())


for i in range(N):
    for j in range(N):
        print(chr(65+N*i+j), end="")
    print()