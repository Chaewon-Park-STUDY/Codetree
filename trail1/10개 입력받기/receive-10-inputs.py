store= list(map(int, input().split()))

my=[]
for i in store:
    if i==0:
        break
    else:
        my.append(i)


avg= sum(my)/len(my)

print(sum(my), round(avg, 1), end= " ")
