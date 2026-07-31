N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.

candid=[]
final_cand=[] 
for i in range(S):
    for j in range(D):
        if p[j]==sick_p[i] and t[j]<sick_t[i]:
            if m[j] not in candid:
                candid.append(m[j])
            final_cand.append((p[j],m[j]))


answer=[] #최종 치즈 교집합

for j in range(len(candid)):
    if all((elem,candid[j]) in final_cand for elem in sick_p):
        answer.append(candid[j])


num= S

for i in range(1,N+1):
    if i not in sick_p:
        for j in range(D):
            if p[j]==i and m[j] in answer:
                num+=1
print(num)
