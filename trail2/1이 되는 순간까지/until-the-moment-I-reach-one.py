N = int(input())

# Please write your code here.

total=0
def calculate(n):
    global total
    while n!=1:
        if n%2==0:
            total+=1
            return calculate(n/2)
        else:
            total+=1
            return calculate(n//3)
    return total

print(calculate(N))

        