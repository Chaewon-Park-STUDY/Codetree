n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class Student():
    def __init__(self, n, s_1, s_2, s_3):
        self.n= n
        self.s_1= s_1
        self.s_2= s_2
        self.s_3= s_3

students=[]

for _ in range(n):
    (n, s_1, s_2, s_3)= (name[_], score1[_], score2[_], score3[_])
    students.append(Student(n,s_1,s_2,s_3))

students.sort(key= lambda x: x.s_1+ x.s_2+x.s_3)

for elem in students:
    print(elem.n, elem.s_1, elem.s_2, elem.s_3)