arr= list(map(int, input().split()))

small=[]
big=[]

for i in range(10):
    if arr[i] <500:
        small.append(arr[i])
    else:
        big.append(arr[i])

max=0
min=1000
for elem in small:
    if elem>= max:
        max= elem
for cnt in big:
    if cnt<= min:
        min= cnt
print(max, min, end= " ")
