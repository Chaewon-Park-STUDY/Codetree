a,b,c= list(map(int, input().split()))

max_val=-100
 
for elem in a,b,c:
    if elem>max_val:
        max_val=elem
print(max_val)