N = int(input())
seats = input()

# Please write your code here.
seats=list(map(int, list(seats)))

available=[]
for i,elem in enumerate(seats):
    if elem==1:
        available.append(i)


store=[]
for i in range(N):
    min_val=1000
    if seats[i]==0:
        new=available.copy()
        new.append(i)
        new.sort()
        for k in range(1,len(new)):
            dist= new[k]-new[k-1]
            min_val=min(min_val,dist)
        store.append(min_val)
print(max(store))
