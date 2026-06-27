a, b, c = map(int, input().split())

# Please write your code here.

num=a*b*c
def logic(num):

    if num<10:
        return num
    return logic(num//10)+ num%10
print(logic(num))