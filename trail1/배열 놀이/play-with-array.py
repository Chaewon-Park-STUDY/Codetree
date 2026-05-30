
arr= list(map(int, input().split()))

N= arr[0]
Q= arr[1]
last=0
store= list(map(int, input().split()))

for i in range(Q):
    question_i= list(map(int,input().split()))
    if question_i[0]== 1:
        print(store[question_i[1]-1])
    elif question_i[0] == 2:
        if store.count(question_i[1])>1:
            for j in range(N):
                if store[j]== question_i[1]:
                    print(j+1)
                    break
        elif store.count(question_i[1])==1:
            for j in range(N):
                if store[j]== question_i[1]:
                    print(j+1)
        else:
            print(0)
    else:
        final= store[question_i[1]-1: question_i[2]]
        for elem in final:
            print(elem, end= " ")
        print()
        #print(*final)