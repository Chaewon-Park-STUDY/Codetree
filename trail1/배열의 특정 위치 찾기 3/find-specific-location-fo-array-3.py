
store= list(map(int, input().split()))

answer=0

for i in range(0, len(store)):
    if store[i]==0:
        answer+=(store[i-1]+store[i-2]+store[i-3])
        break
print(answer)