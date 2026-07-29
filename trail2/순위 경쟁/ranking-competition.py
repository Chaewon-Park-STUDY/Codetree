n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
score=[0,0,0]

rank_A,rank_B,rank_C=1,1,1
award=[]
award.append((0,1,2))

for i in range(n):
    if c[i]=="A":
        score[0]+=s[i]
    elif c[i]=="B":
        score[1]+=s[i]
    else:
        score[2]+=s[i]
    store=[]
    for k in range(3):
        if score[k]==max(score):
            store.append(k)
    award.append(tuple(elem for elem in store))

num=0
for k in range(len(award)-1):
    if award[k]!=award[k+1]:
        num+=1
print(num)