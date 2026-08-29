n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[]
start=0
store=[]
max_val=0
new=0
final=[]

def far(arr):
    global max_val
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            max_val=max(max_val,(arr[i][0]-arr[j][0])**2+ (arr[i][1]-arr[j][1])**2)



def choose(n,m,start):
    global max_val
    if len(arr)==m:
        far(arr)
        final.append(max_val)
        max_val=0
        return final
    for i in range(start,n):
        arr.append(points[i])
        start=i
        choose(n,m,start+1)
        arr.pop()
choose(n,m,start)
print(min(final))