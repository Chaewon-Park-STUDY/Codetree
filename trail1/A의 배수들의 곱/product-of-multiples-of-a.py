A, B= map(int, input().split())

num=1
for i in range(1,B+1):
    if i%A==0:
        num*=i
print(num)
