a,b,c= map(int, input().split())

arr=(a,b,c)
min=100
for elem in arr:
    if elem<min:
        min=elem
print(min)