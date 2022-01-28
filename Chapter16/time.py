class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    
time = Time()
time.hour = 1
time.minute = 6
time.second = 30

t1 = Time()
t1.hour = 7
t1.minute = 40
t1.second = 12

t2 = Time()
t2.hour = 7
t2.minute = 30
t2.second = 59

def print_time(time):
    """Takes a Time object and prints it in the form hour:minute:second"""
    print('%d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
    """Takes 2 time objects, returns True if t1 follows t2 chronologically, otherwise False
    """
    t1_seconds = t1.second + t1.minute*60 + t1.hour*3600
    t2_seconds = t2.second + t2.minute*60 + t2.hour*3600
    return t1_seconds > t2_seconds

print(is_after(t1, t2))
print_time(time)
