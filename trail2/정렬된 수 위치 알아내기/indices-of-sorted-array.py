n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
new=[]
for idx, elem in enumerate(sequence,start=1):
    new.append((idx, elem))


new.sort(key=lambda x: x[1])

for i in range(1,n+1):
    for _ in range(n):
        if new[_][0]==i:
            print(_+1, end=" ")

