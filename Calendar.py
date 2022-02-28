# CALENDAR MODULE
import calendar

# check the weekheader
weekheader = calendar.weekheader(3)
print(weekheader)

# check the month current month calendar
month = calendar.month(2021, 8, w=3)
print(month)

# check the whole year calendar
year = calendar.calendar(2021, w=3)
print(year)

