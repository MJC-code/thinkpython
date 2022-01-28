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
    
birthday = datetime.date(1975, 1, 30)
print(birthday)

print(find_age(birthday))

