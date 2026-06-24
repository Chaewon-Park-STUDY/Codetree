a, b = map(int, input().split())

# Please write your code here.

def evaluate(n):
    return n%3==0 and n%9!=0



def logic(n):
    return n%2!=0 and n%10!=5 and not evaluate(n)

num=0
for i in range(a,b+1):
    if logic(i):
        num+=1
print(num)

