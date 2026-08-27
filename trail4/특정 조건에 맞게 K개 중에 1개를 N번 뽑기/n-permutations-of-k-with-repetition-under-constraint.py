K, N = map(int, input().split())

# Please write your code here.


arr=[]

def print_answer(arr):
    for elem in arr:
        print(elem, end=" ")
    print()


def count_num(arr):
    for i in range(N-2):
        if all(elem==arr[i] for elem in arr[i:i+3]):
            return False
    return True



def choose(K,N):
    if len(arr)==N:
        if count_num(arr):
            return print_answer(arr)
        else:
            return False
    
    for i in range(1,K+1):
        arr.append(i)
        choose(K,N)
        arr.pop()

choose(K,N)
