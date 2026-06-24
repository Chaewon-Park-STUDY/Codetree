n = int(input())

# Please write your code here.

def want_ans(N):
    return N%2==0 and (N//10+ N%10)%5==0

if want_ans(n):
    print("Yes")
else:
    print("No")