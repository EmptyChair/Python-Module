# DATES - import module, show year and day of week

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

### Create datetime object - if time not provided, copied from current time

a = datetime.datetime(2020,9,24)

print(x)

### strftime() method

print(a.now())
print(a.strftime("%B"))

