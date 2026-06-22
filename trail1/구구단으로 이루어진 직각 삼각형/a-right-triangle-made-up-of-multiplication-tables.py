N= int(input())


for i in range(N):
    for j in range(1,N+1-i):
        print(f"{i+1} * {j} = {(i+1)* j}", end=" ")
        if j< N-i:
            print("/", end=" ")
    print()