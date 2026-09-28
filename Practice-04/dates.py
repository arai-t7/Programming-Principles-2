from datetime import datetime, date, timedelta, timezone

# Current date and time
current_time = datetime.now()
print("Current time:", current_time)

# Creating a date object
birthday = date(2007, 5, 15)
print("Birthday:", birthday)

# Formatting a date
formatted_date = current_time.strftime("%d.%m.%Y")
print("Formatted date:", formatted_date)

# Time difference
today = date.today()
difference = today - birthday
print("Days passed:", difference.days)

# Add seven days
next_week = today + timedelta(days=7)
print("Next week:", next_week)

# Kazakhstan timezone UTC+5
kazakhstan_timezone = timezone(timedelta(hours=5))
kazakhstan_time = datetime.now(kazakhstan_timezone)

print("Kazakhstan time:", kazakhstan_time)