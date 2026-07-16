n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

add_sum= sum(blocks)
avg= add_sum//n

num=0
blocks.sort()

for elem in blocks:
    if elem>avg:
        num+=elem-avg
print(num)