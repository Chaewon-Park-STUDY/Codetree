
N= int(input())

num=N
how_many=0

for i in range(1,N):
    num=num//i
    how_many+=1
    if num<=1:
        print(how_many)
        break
