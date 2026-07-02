n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Weather():
    def __init__(self, time, week, forecast):
        self.t= time
        self.w= week
        self.f= forecast


store=[]
new_date=[]

for _ in range(n):
    (time, week, forecast)= (date[_], day[_], weather[_])
    if weather[_]== "Rain":
        new_date.append(date[_])
        store.append(Weather(time,week,forecast))



for _ in range(len(store)):
    if store[_].t== sorted(new_date)[0]:
        print(store[_].t, store[_].w, store[_].f)
