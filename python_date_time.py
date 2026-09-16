from datetime import datetime

now = datetime.now()
# now = datetime(2020, 1, 1, 18, 55, 33)
year = now.year
month = now.month
day = now.day 
hour = now.hour
minute = now.minute
second = now.second
print(second)
print(minute)
print(hour)
print(day)
print(month)
print(year)
print(f'{month}/{day}/{year}')
print(f'{day}/{month}/{year}')

# print(dir(datetime))

t = now.strftime("%#d %a %b %Y %H:%M")
print(t)

t = now.strftime("%#d-%m-%Y %H:%M")
t = now.strftime("%#d/%m/%Y %H:%M")
print(t)

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%#d %B, %Y")
print(type(date_object))
print(date_object.year)
print(date_object.month)


from datetime import date, datetime
today =  datetime(year=2026, month=9, day=13, hour = 22, minute = 25)
new_year =  datetime(year=2027, month=1, day=1, hour = 0, minute = 0)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)