import datetime

seconds = input("Please enter the time in seconds: ")
minutes, sec = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

print('{:d}:{:02d}:{:02d}'.format(hours, minutes, sec))



