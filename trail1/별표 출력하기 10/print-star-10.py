N= int(input())


if N%2!=0:
    for i in range(N):
        if i%2==0 and i<=(N-1):
            for j in range(int(i/2)+1):
                print("*", end= " ")
            print()
        else:
            for j in range(N-int((i-1)/2)):
                print("*", end= " ")
            print()
    for i in range(N):
        if i%2==0 and i<=(N-1):
            for j in range(int((N+1)/2-i/2)):
                print("*", end=" ")
            print()
        else:
            for j in range(int((N+1)/2)+1+int((i-1)/2)):
                print("*", end=" ")
            print()

else:
    for i in range(N):
        if i%2==0:
            for j in range(int(i/2)+1):
                print("*", end=" ")
            print()
        else:
            for j in range(N- int((i-1)/2)):
                print("*", end= " ")
            print()
    for i in range(N):
        if i%2==0:
            for j in range(int(N/2)  + 1 + int(i/2)):
                print("*", end= " ")
            print()
        else:
            for j in range(int(N/2)- int((i-1)/2)):
                print("*", end= " ")
            print()





