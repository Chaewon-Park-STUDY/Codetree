ability = list(map(int, input().split()))

# Please write your code here.
#2명씩 3팀으로

def get_diff(i,j,k,l):
    store=[]
    group_1= ability[i]+ability[j]
    group_2= ability[k]+ability[l]
    group_3= sum(ability)- group_1-group_2
    store.append(group_1)
    store.append(group_2)
    store.append(group_3)
    return max(store)-min(store)

n= len(ability)
new=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if k!=i and k!=j:
                for l in range(k+1,n):
                    if l!=i and l!=j:
                        new.append(get_diff(i,j,k,l))
print(min(new))
