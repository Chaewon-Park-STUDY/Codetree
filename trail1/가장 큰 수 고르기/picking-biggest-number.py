arr= list(map(int, input().split()))

max= 0
for elem in arr:
    if elem>=max:
        max= elem
print(max)