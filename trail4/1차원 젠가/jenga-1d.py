n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.


for i in range(2):
    if i==0:
        for j in range(e1-s1+1):
            blocks.pop(s1-1)
    else:
        for j in range(e2-s2+1):
            blocks.pop(s2-1)

if len(blocks)!=0:
    print(len(blocks))
    for elem in blocks:
        print(elem)
else:
    print(len(blocks))
        