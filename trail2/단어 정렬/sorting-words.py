n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.

arr=sorted(word)
for elem in arr:
    print(elem)