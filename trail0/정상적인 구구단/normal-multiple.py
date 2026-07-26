N= int(input())

for i in range(N):
    for j in range(N):
        if j!=N-1:
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)},",end=" ")
        else:
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)}",end=" ")
    print()