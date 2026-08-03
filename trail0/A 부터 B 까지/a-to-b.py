A,B= map(int, input().split())

a=A


while a<=B:
    print(a, end=" ")
    if a%2!=0:
        a*=2
    else:
        a+=3
   