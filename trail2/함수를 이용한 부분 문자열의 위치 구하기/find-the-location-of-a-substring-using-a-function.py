text = input()
pattern = input()

# Please write your code here.

def logic():
    for j in range(len(text)):
        if text[j:j+len(pattern)]==pattern:
            return j
    return -1
answer=logic()
print(answer)
