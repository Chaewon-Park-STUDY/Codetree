age_first, sex_first= input().split()
age_sec, sex_sec= input().split()
age_first= int(age_first)
age_sec= int(age_sec)

if age_first>=19 and sex_first=="M" or age_sec>=19 and sex_sec=="M":
    print(1)
else:
    print(0)