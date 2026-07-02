MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Name():
    def __init__(self, codename, score):
        self.c= codename
        self.s= score

students=[]

for _ in range(5):
    (codename, score)= codenames[_], scores[_]
    students.append(Name(codename, score))

for _ in range(5):
    if scores[_]==min(scores):
        answer=students[_]
print(answer.c, answer.s)