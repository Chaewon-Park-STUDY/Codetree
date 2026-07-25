N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
#한 학생이 K번 (3번) 이상 벌치기염 볼금

store=[]
num=0

for elem in student:
    store.append(elem)
    if store.count(elem)==K:
        print(elem)
        num+=1
        break
if num!=1:
    print(-1)
