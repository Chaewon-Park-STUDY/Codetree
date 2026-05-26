N= int(input())

number=0

for i in range(N):
    grade_i= list(map(int, input().split()))
    if sum(grade_i)/len(grade_i)>=60:
            print("pass")
            number+=1
    else:
            print("fail")
print(number)