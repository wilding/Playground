from datetime import timedelta

print timedelta.min
print timedelta.max
print timedelta.resolution
print '\n'

interval = timedelta(7, 54, 1234, 5, 5, 5, 5)
print interval
print '\n'

print interval.days
print interval.seconds
print interval.microseconds
print '\n'

print interval.total_seconds()
