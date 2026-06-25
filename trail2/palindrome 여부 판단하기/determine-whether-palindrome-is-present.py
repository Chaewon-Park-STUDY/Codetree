A = input()

# Please write your code here.

def logic(N):
    if N[::]==N[::-1]:
        return "Yes"
    else:
        return "No"

print(logic(A))