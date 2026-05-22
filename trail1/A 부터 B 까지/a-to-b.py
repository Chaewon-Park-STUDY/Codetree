
A,B= map(int, input().split())

i= A
print(i, end= " ")

while A<=i<=B:
    if i%2!=0:
        i*=2
        if i<=B:
            print(i, end= " ")
    else:
        i+=3
        if i<=B:
            print(i, end= " ")