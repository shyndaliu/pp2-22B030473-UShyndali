import datetime as dt
today=dt.date.today()
yesterday=dt.date(today.year, today.month, today.day-1)
tommorow=dt.date(today.year, today.month, today.day+1)
print(yesterday)
print(today)
print(tommorow)