arr = list(map(int, input().split()))

# Please write your code here.

def get_diff(i,j,k):
    store=[]
    sum_1= arr[i]+arr[j]
    sum_2= arr[k]
    sum_3= sum(arr)-sum_1-sum_2
    store.append(sum_1)
    store.append(sum_2)
    store.append(sum_3)

    if sum_1!= sum_2 and sum_1!=sum_3 and sum_2!=sum_3:
        return max(store)-min(store)
    else:
        return 0


n= len(arr)
new=[]
min_val=2000

for i in range(n):
    for k in range(n):
        if k!=i:
            for j in range(n):
                if j!=i and j!=k:
                    new.append(get_diff(i,j,k))


if all(elem==0 for elem in new):
    print(-1)
else:
    for elem in new:
        if elem!=0:
            if elem<min_val:
                min_val=elem
    print(min_val)