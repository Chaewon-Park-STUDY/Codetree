N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
arr=[]
for i in range(N):
    arr.append([P[i],S[i]])



store=[[P[i]+S[i],i]for i in range(N)]
store.sort()


max_num=0
for i in range(N):
    arr[store[i][1]][0]//=2
    total=0
    num=0
    for j in range(N):
        if total+arr[store[j][1]][0]+arr[store[j][1]][1]<=B:
            total+=arr[store[j][1]][0]+arr[store[j][1]][1]
            num+=1

    max_num= max(max_num,num)
    arr[store[i][1]][0]*=2
print(max_num)