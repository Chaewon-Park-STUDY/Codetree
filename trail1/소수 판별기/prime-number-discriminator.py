N= int(input())

if all (N%i!=0 for i in range(2,N)):
    print("P")
else:
    print("C")
