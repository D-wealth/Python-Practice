
# DATETIME MODULES
# import datetime
# import pytz
# today = datetime.date.today()
# print(today)

# birthday = datetime.date(2000, 9, 11)
# print(repr(birthday))

# days_since_birth = (today - birthday).days
# print(days_since_birth)

# # Add days to current day using the timedelta
# tdelta = datetime.timedelta(days = 10)
# print(today + tdelta)

# # HOURS DELTA
# #add 10hours to the current time

# hours_delta = datetime.timedelta(hours=10)
# datetime_today  = datetime.datetime.now() + hours_delta
# print(datetime_today)

# # check the US current time, but before that you need to import PYTZ
# datetime_today = datetime.datetime.now(tz = pytz.UTC)
# print(datetime_today)

# datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
# print(datetime_pacific)
# for tz in pytz.all_timezones:
#     print(tz)




























import datetime
from time import strftime 

now = datetime.date.today()
print(strftime("%d/ %B/ %Y"))

time = datetime.datetime.now()
print(strftime("%d / %m / %Y  %H:%M:%S"))










