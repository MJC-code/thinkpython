import datetime

def find_n_day(older_birthday, younger_birthday, n):
    """Takes 2 datetime.date objects representing different days, returns the date when one is
    twice as old as the other
    Precondition: older_birthday < younger_birthday"""
    assert older_birthday < younger_birthday
    difference = younger_birthday - older_birthday
    n_day = younger_birthday + (difference * 1/(n-1))
    return n_day

birthday1 = datetime.date(1975, 1, 1)
birthday2 = datetime.date(1975, 2, 4)

print('Birthday 1 is', birthday1)
print('Birthday 2 is', birthday2)
n = 4
print(n, 'day for these two birthdays is', find_n_day(birthday1, birthday2, n))





