import calendar
month, day, year = map(int, input().split())
day_of_week = calendar.weekday(year, month, day)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days[day_of_week].upper())
