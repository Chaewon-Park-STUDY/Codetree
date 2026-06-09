A= input()
B= input()

for elem in B:
    if elem=="L":
        new=A[1::]+A[0]
        A=new
    else:
        new=A[-1]+A[:-1]
        A= new
print(new)