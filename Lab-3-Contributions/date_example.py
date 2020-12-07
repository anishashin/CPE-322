from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
first = date(2020, 8, 31)
last = date(2020, 12, 7)
timediff = now - first
print('{:d} days after the first day of classes'.format(timediff.days))
timediff = last - now
print('{:d} days before the last day of classes'.format(timediff.days))

###MODIFIED CODE###
birthday = input("Enter your birthday in the format (YYYY-MM-DD): ")
components = birthday.split("-")
year = int(components[0])
month = int(components[1])
day = int(components[2])
birthday = date(year, month, day)

age = now.year - birthday.year - ((now.month, now.day) < (birthday.month, birthday.day))
print("You are " + str(age) + " years old")

timediff = (now - date(now.year, birthday.month, birthday.day)).days
if timediff < 0:
    timediff = (now - date(now.year-1, birthday.month, birthday.day)).days
print('{:d} days since your last birthday'.format(timediff))

timediff = (date(now.year, birthday.month, birthday.day) - now).days
if timediff < 0:
    timediff = (date(now.year+1, birthday.month, birthday.day) - now).days
print('{:d} days until your next birthday'.format(timediff))
###################
