
arr= list(map(int, input().split()))

score=[]

for num in arr:
    if num>=10:
        score.append(10*(num//10))
    elif num==0:
        break



for i in range(100,0,-10):
    print(f"{i} - {score.count(i)}")