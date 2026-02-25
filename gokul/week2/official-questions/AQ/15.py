# On what day of the week were you born? 
# If you don't know the answer to this, use the calendar library to get the answer.

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
print(calendar.day_name[calendar.weekday(year, month, day)])
