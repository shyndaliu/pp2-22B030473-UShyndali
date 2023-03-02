import datetime as dt
today=dt.date.today()
yesterday=dt.date(today.year, today.month, today.day-1)
tommorow=dt.date(today.year, today.month, today.day+1)
print(dt.date.today()-dt.timedelta(1))
print(today)
print(dt.date.today()+dt.timedelta(1))