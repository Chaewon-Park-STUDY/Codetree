a, b = map(int, input().split())

# Please write your code here.

def calculate(a,b):
    if a>b:
        a+=25
        b*=2
        return a,b
    else:
        a*=2
        b+=25
        return a,b

m,n= calculate(a,b)
print(m,n)