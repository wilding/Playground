from datetime import date


print date.min
print date.max
print date.resolution
print '\n'


birthday = date(1990, 11, 12)
today = date.today()
christmas = date.fromordinal(359)
# from timestamp
print birthday
print today
print christmas
print '\n'


print today.year
print today.month
print today.day
print '\n'


print today > birthday
time_travel = today.replace(year=1970)
print time_travel
print time_travel > birthday
# timedelta stuff
print '\n'


print birthday.strftime("weekday(%%A, %%a, %%w): %A, %a, %w")
print birthday.strftime("day(%%d, %%j): %d, %j")
print birthday.strftime("week(%%U, %%W): %U, %W")
print birthday.strftime("month(%%B, %%b, %%m): %B, %b, %m")
print birthday.strftime("year(%%Y, %%y): %Y, %y")
print birthday.strftime("other(%%x): %x")
# format
print '\n'


print birthday.isoformat()  # equivalent w/ below
print str(birthday)  # equivalent w/ above
print birthday.ctime()
print birthday.toordinal()
print birthday.timetuple()
for i in birthday.timetuple():
    print i
print birthday.isocalendar()
for x in birthday.isocalendar():
    print x
print '\n'


print birthday.weekday()
print birthday.isoweekday()
print '\n'
