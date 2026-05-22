
N= int(input())

for num in range(1, N+1):
    if num%2==0 or num %3==0:
        print(1, end= " ")
    else:
        print(0, end= " ")