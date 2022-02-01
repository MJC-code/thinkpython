class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
   
    def print_time(self):
        print('%d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

    
def is_after(t1, t2):
    """Takes 2 time objects, returns True if t1 follows t2 chronologically, otherwise False
    """
    t1_seconds = t1.second + t1.minute*60 + t1.hour*3600
    t2_seconds = t2.second + t2.minute*60 + t2.hour*3600
    return t1_seconds > t2_seconds

   
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

print(is_after(t1, t2))
t1.print_time()
print(t1.time_to_int())
new_time = t1.increment(354)
new_time.print_time()
print(t1.is_after(t2))
t3 = t1 + 40
print(t3)
t3 = t1 + t2
print(t3)
