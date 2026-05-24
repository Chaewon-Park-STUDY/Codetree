
arr= list(map(int, input().split()))

new=[]

for i in range(0,10):
    if arr[i]<250:
        if all(x < 250 for x in arr[:i]):
            new.append(arr[i])
result= sum(new)
print(result, end= " ")

avg= result/len(new)

print(round(avg,1), end= " ")



    




#아 최초 조건 고려안함
