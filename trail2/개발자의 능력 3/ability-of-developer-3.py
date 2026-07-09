abilities = list(map(int, input().split()))

# Please write your code here.

def get_diff(i,j,k):
    sum_1= abilities[i]+ abilities[j]+abilities[k]
    sum_2= sum(abilities)- sum_1
    return abs(sum_1-sum_2)

n= len(abilities)
new=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            new.append(get_diff(i,j,k))
print(min(new))

        