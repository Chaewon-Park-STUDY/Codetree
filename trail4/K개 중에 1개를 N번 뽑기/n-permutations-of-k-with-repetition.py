K, N = map(int, input().split())

# Please write your code here.



def answer(arr):
    for elem in arr:
        print(elem, end=" ")
    print()



arr=[]
def choose(K,N):
    if len(arr)==N:
        return answer(arr)

    for i in range(1,K+1):
        arr.append(i)
        choose(K,N)
        arr.pop()



choose(K,N)