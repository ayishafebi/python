import time
import datetime
now=datetime.datetime.now()
print("current date and time:",now)
print("current year:",now.year)
print("month of the year:",now.month)
print("week number:",now.strftime("%U"))
print("week day number:",now.weekday())
print("day of year:",now.strftime("%j"))
print("day of the month:",now.day)
print("day of week",now.strftime("%A"))
