n= int(input())

classroom=0
hall=0
restroom=0

for day in range(1,n+1):
    if day%2==0 and day%3!=0 and day%12!=0:
        classroom+=1


    elif day%3==0 and day%12!=0:
        hall+=1
 
    elif day%12==0:
        restroom+=1

print(classroom, end= " ")
print(hall, end= " ")
print(restroom, end= " ")