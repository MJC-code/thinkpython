import datetime

def mul_time(time, number):
    """Takes a Time object and a number, returns a new Time object that contains product of the two"""
    result = Time()
    time = time_to_int(time)
    result = int_to_time(time * number)
    return result

def find_average_pace(time, distance):
    """Takes a Time object representing finishing time and a number representing distance in miles
    Returns a Time object the represents the average pace (time per mile)
    sample input 0:30:0, 2   - returns 0:15:0
    1:20:00 4   returns 0:20:00"""
    return mul_time(time, 1/distance)
    

def print_time(time):
    """Takes a Time object and prints it in the form hour:minute:second"""
    print('%d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
    """Takes 2 time objects, returns True if t1 follows t2 chronologically, otherwise False
    """
    t1_seconds = t1.second + t1.minute*60 + t1.hour*3600
    t2_seconds = t2.second + t2.minute*60 + t2.hour*3600
    return t1_seconds > t2_seconds

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    time_in_seconds = time_to_int(time)
    result = time_in_seconds + seconds
    return int_to_time(result)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if  time.minute >= 60 or time.second >= 60:
        return False
    return True



class Time:
    """Represents the time of day.

    attributes: hour, minute, second"""
    
time = Time()
time.hour = 1
time.minute = 6
time.second = 0

t1 = Time()
t1.hour = 7
t1.minute = 40
t1.second = 12

t2 = Time()
t2.hour = 7
t2.minute = 30
t2.second = 59

today = datetime.date.today()
print(today, today.strftime("%A"))

