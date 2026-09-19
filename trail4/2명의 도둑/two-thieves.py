n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n-m+1):
        value=[]
        for k in range(j,j+m):
                value.append(weight[i][k])
        candid=[]
        def max_val(candid):
            val=0
            if sum(candid)<=c:
                for elem in candid:
                    val+=elem**2
            return val

        for l in range(1,len(value)+1):
            def dfs(start):
                if len(candid)==l:
                    arr[i][j]=max(arr[i][j],max_val(candid))
                    return 
                for p in range(start,len(value)):
                    candid.append(value[p])
                    start=p
                    dfs(start+1)
                    candid.pop()
            dfs(0)

if 2*m<=n:
    store=[]
    answer=0

    def repeat():
        global answer
        if len(store)==2:
            A=store[0]
            B=store[1]
            if A==B:
                for i in range(n-m):
                    sum_val=0
                    sum_val+=arr[A][i]
                    sum_val+=arr[A][i+m]
                    answer=max(answer,sum_val)
            else:
                answer=max(answer,max(arr[A])+max(arr[B]))
            return 
        for i in range(n):
            store.append(i)
            start=i
            repeat()
            store.pop()
    repeat()



else:
    store=[]
    answer=0

    def repeat(start):
        global answer
        if len(store)==2:
            A=store[0]
            B=store[1]
            answer=max(answer,max(arr[A])+max(arr[B]))
            return 
        for i in range(start,n):
            store.append(i)
            start=i
            repeat(start+1)
            store.pop()
    repeat(0)
print(answer)