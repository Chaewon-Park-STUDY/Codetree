
B,A= map(int, input().split())

i= B

while A<=i<=B:
    if i%2==0:
        print(i, end= " ")
    i-=2