N= int(input())


for i in range(1,N+1):
    if i==1 or i==N:
        for j in range(N-1):
            print("*",end=" ")
        print("*")
    else:
        for j in range(i-1):
            print("*", end=" ")
        for k in range(N-i):
            print(" ", end=" ")
        print("*")
