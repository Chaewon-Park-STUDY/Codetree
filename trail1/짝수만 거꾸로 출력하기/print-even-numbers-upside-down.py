
N= int(input())
given= list(map(int, input().split()))

new=[]
for i in given:
    if i %2==0:
        new.append(i)
    else:
        pass


result= new[len(new)-1::-1]

for num in result:
    print(num, end= " ")