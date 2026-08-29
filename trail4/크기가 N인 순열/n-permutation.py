n = int(input())

# Please write your code here.


def print_answer(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

arr=[]
start=1
for i in range(1,n+1):
    arr.append(i)
    def choose(n):
        if len(arr)==n:
            return print_answer(arr)

        for j in range(1,n+1):
            if j not in arr:
                arr.append(j)
                choose(n)
                arr.pop()
    choose(n)
    arr.pop()