
my= list(map(int, input().split()))

new=[]
how_many=0

for i in my:
    if i==0:
        break
    else:
        if i%2==0:
            new.append(i)
            how_many+=1
print(how_many, sum(new), end= " ")       
