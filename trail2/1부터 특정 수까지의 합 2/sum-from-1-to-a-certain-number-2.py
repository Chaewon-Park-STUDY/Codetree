N = int(input())

# Please write your code here.
total=0
def gauss(N):
    global total
    if N==0:
        return 0
    total+=N
    gauss(N-1)
    return total

print(gauss(N))