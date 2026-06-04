A, B= map(int, input().split())

num=0

for i in range(A, B+1):
    if i%6==0 and i%8!=0:
        num+=i
print(num)
