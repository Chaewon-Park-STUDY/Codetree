N= int(input())



for i in range(N):
    for j in range(10+2*i+1,10+2*i+(2*(N-1))+2, 2):
        print(j, end= " ")
    print()