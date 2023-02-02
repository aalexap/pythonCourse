import calendar
# print(calendar.month(2023, 1, w=10, l=2))
# print(calendar.calendar(2023, c=10, m=4))
# print(calendar.weekday(2023, 1, 27))
# print(calendar.isleap(2023))
# print(calendar.leapdays(2000, 2020))
# print(calendar.HTMLCalendar().formatmonth(2023, 1))

# import time
# start = time.time()
# # time.sleep(5)
# print(time.asctime())
# print(time.gmtime())
# print(type(time.localtime()))
# print(time.localtime())
# stop = time.time()
# print(stop - start)

import datetime

# d = datetime.date(2021, 1, 27)
# print(d)
# today = datetime.date.today()
# print(today)
# print(today.weekday())
# print(today.isoweekday())
# print(today - d)
#
# tdelta = datetime.timedelta(days=365.25, minutes=12, hours=36)
# print(tdelta.days)
# print(tdelta.total_seconds())


# t = datetime.time(14, 25, 10, 456)
# tdelta - datetime.timedelta(minutes=5)

# dt = datetime.datetime(2020, 11, 3, 12, 23, 12)
# print(dt.time())
# print(dt.date())
#
# tdelta = datetime.timedelta(days=7, hours=15, minutes=33)
# print(dt - tdelta)

today = datetime.datetime.now()
print(today)

print(today.strftime('%A %d/%m/%Y'))  # https://docs.python.org/3/library/datetime.html

dt_str = 'November 30, 2020 15:23'

new_date = datetime.datetime.strptime(dt_str, '%B %d, %Y %H:%M')
print(new_date)
print(type(new_date))


print(today.timestamp())
print(datetime.datetime.fromtimestamp(1674845594.494838))
