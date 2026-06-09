arr=input()
L= len(arr)
print(arr)

for i in range(L):
    new= arr[-1] + arr[:L-1]
    arr=new

    print(new)