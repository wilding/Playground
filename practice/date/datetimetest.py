from datetime import datetime, date, time


print datetime.min
print datetime.max
print datetime.resolution
print '\n'


random = datetime(2016, 9, 11, 14, 58, 34, 123456)  # tz
today = datetime.today()
now = datetime.now()  # tz
utc = datetime.utcnow()
# from timestamp, utc from timestamp
christmas = datetime.fromordinal(359)
new_datetime = datetime.combine(date.today(), time(16, 58, 59, 123456))  # tz
strp_datetime = datetime.strptime('11/12/1990, 2:45:08.123456 PM', '%m/%d/%Y, %I:%M:%S.%f %p')
print random
print today
print now
print utc
print christmas
print new_datetime
print strp_datetime
print '\n'


print today.year
print today.month
print today.day
print today.hour
print today.minute
print today.second
print today.microsecond
print today.tzinfo  # tz
print '\n'


print today.date()
print today.isocalendar()
print today.toordinal()
print today.weekday()
print today.isoweekday()
print today.time()
print today.timetz()  # tz
print '\n'

print today.isoformat('!')  # equivalent to below
print str(today)  # equivalent to above
print today.ctime()
print today.replace(year=1994, hour=12)
print today.timetuple()
print today.utctimetuple()
print '\n'

# format
print today.strftime("year(%%Y, %%y): %Y, %y")
print today.strftime("month(%%B, %%b, %%m): %B, %b, %m")
print today.strftime("week(%%U, %%W): %U, %W")
print today.strftime("weekday(%%A, %%a, %%w): %A, %a, %w")
print today.strftime("day(%%d, %%j): %d, %j")
print today.strftime("hour(%%H, %%I, %%p): %H, %I, %p")
print today.strftime("minute(%%M): %M")
print today.strftime("second(%%S): %S")
print today.strftime("microsecond(%%f): %f")
print today.strftime("timezone(%%z, %%Z): %z, %Z")  # tz
print today.strftime("full(%%c, %%x, %%X): %c, %x, %X")
print '\n'


# today.astimezone()
# today.utcoffset
# today.dst
# today.tzname


# operations
