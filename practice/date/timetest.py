from datetime import time


print time.min
print time.max
print time.resolution
print '\n'


noon = time(12)
random = time(18, 58, 14, 123456)  # tz
print noon
print random
print '\n'


print random.hour
print random.minute
print random.second
print random.microsecond
print random.tzinfo  # tz
print '\n'


print noon < random
time_dict = {noon: 'noon', random: 'randomtime'}
print time_dict
print '\n'


new = random.replace(minute=32, second=59, microsecond=111)
print new
print '\n'


# format
print random.strftime("hour(%%H, %%I, %%p): %H, %I, %p")
print random.strftime("minute(%%M): %M")
print random.strftime("second(%%S): %S")
print random.strftime("microsecond(%%f): %f")
print random.strftime("timezone(%%z, %%Z): %z, %Z")  # tz
print random.strftime("other(%%X): %X")
print '\n'


print random.isoformat()  # equivalent to below
print str(random)  # equivalent to above
print '\n'


print random.utcoffset()  # tz
print random.dst()  # tz
print random.tzname()  # tz
print '\n'
