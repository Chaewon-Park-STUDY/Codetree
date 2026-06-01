n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
b=[]
b=a[::-1]


print(b[0], b[1], end= " ")



