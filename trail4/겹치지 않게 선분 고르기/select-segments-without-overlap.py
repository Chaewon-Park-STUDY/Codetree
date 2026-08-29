n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.

def not_intersect(a,b,c,d):
    return b<c or d<a


max_val=0
for i in range(n):
    arr=[i]

    for j in range(0,n):
        if j not in arr:
            if all(not_intersect(x1[elem],x2[elem],x1[j],x2[j]) for elem in arr):            
                arr.append(j)
    max_val=max(max_val,len(arr))
print(max_val)