n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
# 빙산들이 물에 잠기지 않은 채로 붙어있는 경우를 한 덩어리로
# for i in range(1, max(h)+1):
# 각 h[_]- i를 했을 때 <=0 이면 다 0으로 표시
# 0 이 아닌 연속된 양의 정수 덩어리를 세야함
max_num=0

for i in range(1,max(h)):
    new=[0 for _ in range(n)]
    for j in range(n):
        new[j]=h[j]-i
        if new[j]<=0:
            new[j]=0
    cnt=0

    for k in range(n-1):
        if new[k]!=0 and new[k+1]==0:
            cnt+=1
    
        if all(new[elem]!=0 for elem in range(k+1,n)):
            cnt+=1
            break

    max_num= max(max_num,cnt)
print(max_num)


            

