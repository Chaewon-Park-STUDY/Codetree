
arr= list(map(int, input().split()))

for i in range(1,7):
    print(f"{i} - {arr.count(i)}")