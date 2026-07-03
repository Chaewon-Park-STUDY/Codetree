n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class Student:
    def __init__(self, n,h,w):
        self.n= n
        self.h= h
        self.w= w
students=[]

for _ in range(n):
    (n,h,w)= (name[_], height[_], weight[_])
    students.append(Student(n,h,w))

students.sort(key= lambda x: x.h)
for elem in students:
    print(elem.n, elem.h, elem.w)