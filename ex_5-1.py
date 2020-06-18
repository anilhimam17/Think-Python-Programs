import datetime as dt

#GMT Epoch for Unix
gmt_time = dt.date(1970, 1, 1)

#Present date
pre_time = dt.date.today()

#No of days in btw
no_of_days = (pre_time - gmt_time).days

#No of hours
hours = no_of_days * 24

#No of minutes
mins = hours * 60

#No of seconds
sec = mins * 60

print(f"No of days: {no_of_days}")
print(f"No of hours: {hours}")
print(f"No of mins: {mins}")
print(f"No of secs: {sec}")
