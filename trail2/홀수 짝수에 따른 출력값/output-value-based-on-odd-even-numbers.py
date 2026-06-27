N = int(input())

# Please write your code here.


def logic(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n%2!=0:
        return logic(n-2)+n
    else:
        return logic(n-2)+n
print(logic(N))