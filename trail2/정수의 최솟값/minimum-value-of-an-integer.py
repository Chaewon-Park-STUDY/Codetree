a, b, c = map(int, input().split())

# Please write your code here.

def minimum(a,b,c):
    i=100
    arr=[]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    for elem in arr:
        if elem<i:
            i=elem
    return i

answer= minimum(a,b,c)
print(answer)