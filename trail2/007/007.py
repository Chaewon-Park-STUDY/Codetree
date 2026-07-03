secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.



class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.s= f"secret code : {secret_code}"
        self.m= f"meeting point : {meeting_point}"
        self.t= f"time : {time}"
    
new= Secret(secret_code, meeting_point, time)
print(new.s)
print(new.m)
print(new.t)
