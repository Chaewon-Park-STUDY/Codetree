A = input()
B = input()

# Please write your code here.

new=list(A)
find= list(B)
game_is_on= True


if B in A:
    while game_is_on:
        new=new
        for i in range(len(new)-len(find)+1):
            if all(new[i+j]==find[j] for j in range(len(find))):
                for j in range(len(find)):
                    new.pop(i)
                s=''.join(new)
                break
        if B not in s:
            game_is_on= False

    for elem in new:
        print(elem,end="")
else:
    for elem in new:
        print(elem,end="")