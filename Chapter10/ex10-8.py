import random

def birthday(n):
    """Returns true if a random list of ints from 1 to 365 has a duplicate"""
    birthdays = []
    for i in range(n):
        birthdays.append(random.randint(1, 365))
    birthdays.sort()
    for i in range(n-1):
        if birthdays[i] == birthdays[i+1]:
            return True
    return False


def test_birthdays(number_people, number_of_tests):
    """Calls birthday(number_of_people) number_of_tests times, returns percentage
    of True results"""
    counter = 0
    for i in range(number_of_tests):
        if birthday(number_people):
            counter += 1
    return counter / number_of_tests * 100

for i in(1, 5, 10, 20, 23, 30, 40, 50, 60, 70, 75, 100, 200, 300, 350):
    print(i, '\t', (test_birthdays(i, 5000)))
