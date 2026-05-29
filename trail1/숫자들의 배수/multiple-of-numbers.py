N= int(input())

store=[]

num=0

for i in range(1,100):
    store.append(N*i)


for cnt in store:
    if cnt%5!=0:
        print(cnt, end= " ")
    else:
        print(cnt, end= " ")
        num+=1
        if num==2:
            break