import datetime as dt
def diff(x,y):
    ans=y.timestamp()-x.timestamp()
    return ans

date1=dt.datetime(2022,1,23,15,15,0)
date2=dt.datetime(2022,1,23,15,16,30)
print(diff(date1,date2))
