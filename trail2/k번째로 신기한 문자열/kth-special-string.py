n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
new=[]

for elem in str:
    if elem[:len(t)]== t:
        new.append(elem)

store= sorted(new)
print(store[k-1])