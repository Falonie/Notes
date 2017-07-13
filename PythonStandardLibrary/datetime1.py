from datetime import datetime,timedelta,timezone

#to print current date
print(datetime.now())
print(type(datetime.now()))
now=datetime.now()

#to print spcifield date
t=datetime(2000,1,1,1,1)
print(t)
#convert datetime to timestamp
print(t.timestamp())
print(now.timestamp())

#convert stamp to date
t=2333333333.0
print(datetime.fromtimestamp(t))
print(datetime.fromtimestamp(6666666666))
print(datetime.utcfromtimestamp(t))

#convert string to datetime
cday=datetime.strptime('2333-3-3,3:33:33','%Y-%m-%d,%H:%M:%S')
print(cday)
#converet datetime to string
print(datetime.now().strftime('%a,%b %d %H:%M'))
print(now.strftime('%a,%b %d %H:%M'))

#to plus hours/days
print(now+timedelta(hours=10),now+timedelta(days=1,hours=10))

#convert UTC time to local time
tz_utc_8=timezone(timedelta(hours=8))#create timezone UTC+8:00
dt=now.replace(tzinfo=tz_utc_8)#set timezone as UTC+8:00
print(dt)

#print(datetime.now())
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)