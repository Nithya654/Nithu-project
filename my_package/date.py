import datetime

# Current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

# Current date
current_date = datetime.date.today()
print(f"Current date: {current_date}")

# Formatting the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_datetime}")

# Parsing a date string
date_string = "2025-04-16 14:30:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime: {parsed_datetime}")

# Adding 5 days to the current date
new_date = current_date + datetime.timedelta(days=5)
print(f"New date after adding 5 days: {new_date}")

# Getting the year, month, and day
current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day
print(f"Year: {current_year}, Month: {current_month}, Day: {current_day}")

# Subtracting dates
date1 = datetime.date(2025, 4, 1)
date2 = datetime.date(2025, 4, 16)
date_difference = date2 - date1
print(f"Difference between {date2} and {date1}: {date_difference.days} days")


import datetime

# Get current time
current_time = datetime.datetime.now().time()

# Different formatting options
formatted_time_12hr = current_time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
formatted_time_24hr = current_time.strftime("%H:%M:%S")    # 24-hour format
formatted_time_with_microseconds = current_time.strftime("%H:%M:%S.%f")  # With microseconds

print(f"Formatted time (12-hour format): {formatted_time_12hr}")
print(f"Formatted time (24-hour format): {formatted_time_24hr}")
print(f"Formatted time with microseconds: {formatted_time_with_microseconds}")
