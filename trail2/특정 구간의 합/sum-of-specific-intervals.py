n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


def logic(A,queries):
    global arr
    for elem in queries:
        total=0
        for i in range(elem[0]-1,elem[1]):
            total+=arr[i]
        print(total)
logic(arr,queries)

