n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(int((n+1)/2)):
    new=[]
    for j in range(2*i+1):
        new.append(arr[j])
    index= sorted(new)
    print(index[int((len(index)+1)/2) -1], end=" ")