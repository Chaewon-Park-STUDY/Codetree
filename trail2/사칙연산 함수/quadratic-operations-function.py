a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def summation(a,c):
    return f"{a} + {c} = {a+c}"
def subtract(a,c):
    return f"{a} - {c} = {a-c}"
def multiply(a,c):
    return f"{a} * {c} = {a*c}"
def division(a,c):
    return f"{a} / {c} = {a//c}"

def not_one(N):
    return False

if o=="+":
    print(summation(a,c))
elif o=="-":
    print(subtract(a,c))
elif o=="/":
    print(division(a,c))
elif o=="*":
    print(multiply(a,c))
else:
    print(not_one(o))