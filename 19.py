#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

months=[31,28,31,30,31,30,31,31,30,31,30,31]

days=['tue','wed','thu','fri','sat','sun','mon'] # 1st of Jan 1901 is a Tuesday :)

day=1
sun_count=0

def leapda(year):
    leap=True
    if year%4 !=0:
        leap=False
    elif year%400 !=0:
        leap=False
    return leap

for year in range(1901,2001):
    leap=leapda(year)
    for m in range(12):
        dayName=days[day%7]
        if dayName=='sun':
            sun_count+=1
        day+=months[m]
        if leap==True and months[m]==28:
            day+=1

print(sun_count)  # Answer: 171

'''
# Easy method
from datetime import date

sundays=0
for y in range(1901,2001):
    for m in range(1,13):
        if date(y,m,1).weekday()==6:
            sundays+=1

print(sundays)
'''


