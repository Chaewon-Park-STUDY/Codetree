n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def logic(store):
    for i in range(len(store)):
        if store[i]%2==0:
            store[i]//=2

logic(arr)

for _ in arr:
    print(_, end=" ")