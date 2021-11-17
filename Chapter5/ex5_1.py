"""Prints days since epoch (1 Jan 1970) and
   current GMT time in hours, minutes and seconds"""
import time
t = time.time()

print('Seconds since epoch: ', t)

days_since_epoch = int(t // (24 * 60 * 60)) # t/seconds in a day
print('Days since epoch: ', days_since_epoch)

seconds_in_current_day = t % (24 * 60 * 60)

hour = seconds_in_current_day // (60 * 60)

remaining_seconds = seconds_in_current_day % (60 * 60)

minute = remaining_seconds // 60

second = int(remaining_seconds % 60)

print(f'Current GMT time is: {hour:.0f}:{minute:.0f}:{second:02d}')
