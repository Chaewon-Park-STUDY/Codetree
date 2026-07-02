unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Code():
    def __init__(self,unlock, wire, second):
        self.u= unlock
        self.w= wire
        self.s= second

answer=Code(unlock_code, wire_color, seconds)
print(f"code : {answer.u}\ncolor : {answer.w}\nsecond : {answer.s}")