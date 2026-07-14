N = int(input())
seats = input()

# Please write your code here.
seats=list(map(int, list(seats)))
store=[]

for i in range(N):
    if seats[i]==1:
        store.append(i)

cand=[]
for i in range(N):
    new=store.copy()
    min_val=10000
    if seats[i]==0:
        new.append(i)
        new.sort()
        for k in range(1,len(new)):
            dist=new[k]-new[k-1]
            min_val= min(min_val,dist)
        cand.append(min_val)
print(max(cand))
