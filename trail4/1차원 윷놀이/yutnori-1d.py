n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
store=[]

def count_num(dp):
    return dp.count(m)

max_val=0

def adding(arr):
    global max_val
    pos=[1 for _ in range(k+1)] #말의 시작 위치
    store.append(tuple(arr))
    a=store[0]
    for i in range(n):
        if pos[a[i]]<m:
            pos[a[i]]+=nums[i]
            if pos[a[i]]>m:
                pos[a[i]]=m
    store.pop()
    max_val=max(max_val,count_num(pos))

arr=[]

def choose(k,n):
    if len(arr)==n:
        return adding(arr)

    for i in range(1,k+1):
        arr.append(i)
        choose(k,n)
        arr.pop()

choose(k,n)



print(max_val)
    
