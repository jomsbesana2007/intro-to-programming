## Exercise 3: Print date and Time

# Write a Python program to display the current date and time.

import datetime

time_now = datetime.datetime.now()

print(f"The date today is: {time_now.month}/{time_now.day}/{time_now.year}\n")
print(f"The current  time is: {time_now.hour}:{time_now.minute}:{time_now.second}")

# Python Datetime source: https://www.w3schools.com/python/python_datetime.asp