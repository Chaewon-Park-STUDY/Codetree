cnt_1=[]
cnt_2=[]

for i in range(3):
    arr= list(map(int, input().split()))
    cnt_1.append(arr)


for j in range(2,6):
    arr= list(map(int, input().split()))
    cnt_2.append(arr)
    
cnt_2.remove(cnt_2[0])  

for i in range(3):
    for j in range(3):
        print(cnt_1[i][j]* cnt_2[i][j], end= " ")
    print()

