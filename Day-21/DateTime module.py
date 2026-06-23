from datetime import date,time,datetime,timedelta
t=date.today()
print(t)
print("year:",t.year)
print("Month:",t.month)
print("Day:",t.day)
print("Weekday from 0:",t.weekday())
print("Weekday from 1:",t.isoweekday())


'''#OUTPUT:
2026-06-23
year: 2026
Month: 6
Day: 23
Weekday from 0: 1
Weekday from 1: 2
'''

from datetime import date,time,datetime,timedelta
t=date(2026,12,30)
print(t)


'''#OUTPUT:
2026-12-30'''



from datetime import date,time,datetime,timedelta
t=time(23,59,0)
print(t)

'''#OUTPUT:
23:59:00'''



from datetime import date,time,datetime,timedelta
t=datetime.now()
print(t)
print("year:",t.year)
print("Month:",t.month)
print("Day:",t.day)
print("Hours:",t.hour)
print("Minutes:",t.minute)
print("Seconds:",t.second)

'''#OUTPUT:
2026-06-23 11:39:56.614494
year: 2026
Month: 6
Day: 23
Hours: 11
Minutes: 39
Seconds: 56
'''

from datetime import date, time, datetime, timedelta

n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %Y %I:%M:%S %p'))
print(n.strftime('%a, %d %b, %Y %I:%M:%S %p'))
print(n.strftime('%A, %d %B, %Y %I:%M:%S %p'))

'''#OUTPUT:
23/06/26
23/06/26 11:47:42
23/06/26 11:47:42 AM
23 Jun 26 11:47:42 AM
23 June 2026 11:47:42 AM
Tue, 23 Jun, 2026 11:47:42 AM
Tuesday, 23 June, 2026 11:47:42 AM'''


from datetime import date, time, datetime, timedelta

n = datetime.now()

n15 = n + timedelta(minutes=15)
n2 = n + timedelta(hours=2)
n7 = n + timedelta(days=60)

print(n15, n2, n7, sep='\n')

'''#OUTPUT:
2026-06-23 12:16:35.784608
2026-06-23 14:01:35.784608
2026-08-22 12:01:35.784608'''
