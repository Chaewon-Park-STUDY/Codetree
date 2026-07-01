user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class Store():
    def __init__(self, user2_id= "codetree", user2_level= 10):
        self.id= f"user {user2_id}"
        self.level= f"lv {user2_level}" 
    
default= Store()
print(default.id, end=" ")
print(default.level, end=" ")
print()
num_1= Store(user2_id, user2_level)
print(num_1.id, end=" ")
print(num_1.level, end=" ")