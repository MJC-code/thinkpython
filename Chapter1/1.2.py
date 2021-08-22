seconds = 60*42 + 42
speed_kmph = 10 / (seconds/3600.0)
print("Speed in km/h is", speed_kmph)
speed_mph = speed_kmph / 1.61
print("Speed in mph is", speed_mph)
print("Average pace is", 60/speed_mph, "minutes per mile")

