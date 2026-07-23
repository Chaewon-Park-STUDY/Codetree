n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def logic(a,b):
    num=0
    for i in range(n1-n2+1):
        if all(a[i+j]==b[j] for j in range(n2)):
                num+=1
    if num>0:
        return True

if logic(a,b)==True:
    print("Yes")
else:
    print("No")