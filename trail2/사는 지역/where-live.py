n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.

class Logic():
    def __init__(self, profile, address, living):
        self.n= profile
        self.a= address
        self.l= living
renew= sorted(name)



store=[]

for i in range(n):
    (profile, address, living)= (name[i], street_address[i], region[i])
    store.append(Logic(profile, address, living))

for _ in range(n):
    if renew[n-1]==name[_]:
        answer= store[_]

print(f"name {answer.n}\naddr {answer.a}\ncity {answer.l}")


