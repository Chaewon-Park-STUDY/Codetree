a, b = map(int, input().split())

# Please write your code here.

def prime(n):
    if all (n%i!=0 for i in range(2,n)):
        return True
def is_even(n):
    if n!=100:
        if (n//10+ n%10)%2==0:
            return True
    else:
        return False
num=0
for i in range(a,b+1):
    if prime(i) and is_even(i):
        num+=1
print(num)
