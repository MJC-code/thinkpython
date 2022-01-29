import datetime


def find_age(birthday):
    """Takes a Date object, representing user's birthday
    Prints user's age and number of days, hours, minutes, seconds until next birthday"""
    assert isinstance(birthday, datetime.date)
    today = datetime.date.today()
    age = today.year - birthday.year
    if (birthday.month, birthday.day) > (today.month, today.day):
        age -= 1
    return age

def find_time_to_next_birthday(birthday):
    """Takes a Date object representing  birthday
    Returns timedelta object giving time from current time until next birthday"""
    
    assert isinstance(birthday, datetime.date)
    today = datetime.datetime.now()
    
    birthday = datetime.datetime.combine(birthday, datetime.datetime.min.time())
    
    next_birthday = datetime.datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime.datetime(today.year+1, birthday.month, birthday.day)

    return next_birthday - today

birthday = datetime.date(1975, 6, 30)

print('Birthday is', birthday)
print('Current age is', find_age(birthday))

days_to_birthday = find_time_to_next_birthday(birthday).days
seconds_to_birthday = find_time_to_next_birthday(birthday).seconds

minutes_to_birthday, seconds_to_birthday = divmod(seconds_to_birthday, 60)
hours_to_birthday, minutes_to_birthday = divmod(minutes_to_birthday, 60)

print('Time to next birthday is',  days_to_birthday, 'days,', hours_to_birthday, 'hours,',
      minutes_to_birthday, 'minutes and', seconds_to_birthday, 'seconds.')






