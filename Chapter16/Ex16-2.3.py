import datetime

def find_double_day(older_birthday, younger_birthday):
    """Takes 2 datetime.date objects representing different days, returns the date when one is
    twice as old as the other
    Precondition: older_birthday < younger_birthday"""
    assert younger_birthday > older_birthday
    difference = younger_birthday - older_birthday
    double_day = younger_birthday + difference
    return double_day

birthday1 = datetime.date(1975, 1, 1)
birthday2 = datetime.date(1976, 1, 1)

print('Birthday 1 is', birthday1)
print('Birthday 2 is', birthday2)
print('Double day for these two birthdays is', find_double_day(birthday1, birthday2))





