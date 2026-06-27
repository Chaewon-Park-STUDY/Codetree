n = int(input())

# Please write your code here.

total=0

def calculation(n):
    global total
    if n==1:
        return 0
    if n%2==0:
        calculation(n/2)
        total+=1
    else:
        calculation(n*3+1)
        total+=1
    return total
print(calculation(n))

