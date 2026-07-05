n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

arr=[0 for _ in range(n)]

for elem in commands:
    for i in range(elem[0], elem[1]+1):
        arr[i-1]+=1

print(max(arr))
