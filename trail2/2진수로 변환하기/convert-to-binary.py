n = int(input())

# Please write your code here.
arr=[]
while True:
    if n<2:
        arr.append(n)
        break
    arr.append(n%2)
    n//=2

for elem in arr[::-1]:
    print(elem,end="")
