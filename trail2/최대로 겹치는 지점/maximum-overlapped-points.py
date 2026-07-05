n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[0 for _ in range(100)]
for elem in segments:
    for i in range(elem[0], elem[1]+1):
        arr[i-1]+=1
print(max(arr))