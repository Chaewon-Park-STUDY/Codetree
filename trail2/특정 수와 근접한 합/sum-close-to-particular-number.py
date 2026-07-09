N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

new=[]
for i in range(N-1):
    for j in range(i+1,N):
        sum_value=0
        for elem in arr:
            if elem!=arr[i] and elem!=arr[j]:
                sum_value+=elem
        new.append(sum_value)


store=[]              
for elem in new:
    store.append(abs(S-elem))
print(min(store))