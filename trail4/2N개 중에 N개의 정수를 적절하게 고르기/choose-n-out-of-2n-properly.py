n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

total=sum(num)

store=[]

def sum_val(arr):
    a=sum(arr)
    store.append(abs(a-(total-a)))


arr=[]
start=0

def choose(start,n):
    if len(arr)==n:
        return sum_val(arr)

    for i in range(start,2*n):
        arr.append(num[i])
        start=i
        choose(start+1,n)
        arr.pop()

choose(start,n)
print(min(store))

