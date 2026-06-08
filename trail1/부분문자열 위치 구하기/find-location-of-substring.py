input_str = input()
target_str = input()

# Please write your code here.

for i in range(len(input_str)-(len(target_str)-1)):
    if all(input_str[i+j]== target_str[j] for j in range(len(target_str))):
        print(i)
        break

if target_str not in input_str:
    print(-1)
