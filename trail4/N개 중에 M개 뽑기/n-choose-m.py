N, M = map(int, input().split())

# Please write your code here.

def print_answer(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

arr=[]

start=1
def choose(N,M,start):
    if len(arr)==M:
        return print_answer(arr)

    for i in range(start,N+1):
        arr.append(i)
        start=i
        choose(N,M,start+1)
        arr.pop()
choose(N,M,start)