n = int(input())

# Please write your code here.

def logic(N):
    sum_of=0
    for _ in range(1,N+1):
        sum_of+=_
    return (sum_of//10)
        
final= logic(n)
print(final)