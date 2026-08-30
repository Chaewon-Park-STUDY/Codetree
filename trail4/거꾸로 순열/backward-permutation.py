n = int(input())

# Please write your code here.

def print_answer(arr):
    for elem in arr:
        print(elem, end=" ")
    print()


arr=[]

for i in range(n,0,-1):
    arr.append(i)

    def choose(n):
        if len(arr)==n:
            return print_answer(arr)
        for i in range(n,0,-1):
            if i not in arr:
                arr.append(i)
                choose(n)
                arr.pop()
    choose(n)
    arr.pop()
