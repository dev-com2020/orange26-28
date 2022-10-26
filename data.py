from datetime import date, datetime, timedelta, timezone
import time
import calendar as cal
import arrow
import pytz as pytz

dzis = date.today()
print(dzis)
print(dzis.year)
print(dzis.ctime())
print(dzis.isoformat())
print(dzis.weekday())
kalendarz = cal.day_name[dzis.weekday()]
print(kalendarz)
print(dzis.timetuple())

czas = time.ctime()
print(czas)
print(time.gmtime())
print(time.localtime())

teraz = datetime.now()
print(teraz)
utc = datetime.utcnow()


print(teraz.date())
# time.sleep(5)
print(utc)

strzala = arrow.utcnow()
print(strzala)
print(strzala.now())
local = arrow.now('Asia/Tokyo')
print(local)
print(local.for_json())

time_str = time.strftime("%d-%m-%Y\n%H:%M:%S")
print(time_str)


tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

tz_Warsaw = pytz.timezone('Europe/Warsaw')
datetime_Waw = datetime.now(tz_Warsaw)
print("Warsaw time:", datetime_Waw.strftime("%H:%M:%S"))