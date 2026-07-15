n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
num=0
score_A=0
score_B=0
store=[0]

for i in range(n):
    if c[i]=="A":
        score_A+=s[i]
       
    else:
        score_B+=s[i]
    store.append(score_A-score_B)

if all(s[i]==0 for i in range(n)):
    print(0)
else:
    for i in range(n):
            if store[i]*store[i+1]>0:
                pass
            else:
                num+=1
    print(num)