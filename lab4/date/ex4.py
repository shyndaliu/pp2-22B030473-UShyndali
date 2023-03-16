import datetime as dt
def diff(x,y):
    ans=y.timestamp()-x.timestamp()
    return ans


date2=dt.datetime.today()
date1=date2-dt.timedelta(10)
print(diff(date1,date2))
