n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

class Student:
    def __init__(self, h,w,r):
        self.h= h
        self.w= w
        self.r= r

students.sort(key=lambda x:(x[0],-x[1]))

for elem in students:
    for _ in elem:
        print(_, end=" ")
    print()