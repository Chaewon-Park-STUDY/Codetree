n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class Student:
    def __init__(self, n,k,e,m):
        self.n= n
        self.k= k
        self.e= e
        self.m= m

students=[]

for _ in range(n):
    (n,k,e,m)= (name[_], korean[_], english[_], math[_])
    students.append(Student(n,k,e,m))

students.sort(key=lambda x: (-x.k, -x.e, -x.m))

for elem in students:
    print(elem.n, elem.k, elem.e, elem.m)