n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
x,y= r-1,c-1
store={}
store["R"]= 0
store["D"]=1
store["U"]=2
store["L"]=3

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for key in store:
    if d==key:
        dir_num=store[key]

time=0
while time<t:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    time+=1
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]
    if time==t:
        break

print(x+1,y+1)