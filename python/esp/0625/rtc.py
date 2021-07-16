import machine

import time
import ntptime

n_time = time.localtime(ntptime.time() + 28800)
print(n_time)  # (year,month,day,hours,minutes,seconds,weekdays,subseconds)

rtc = machine.RTC()
rtc.datetime(n_time[0:3] + (0, ) + n_time[3:6] + (0, ))
print(rtc.datetime())
# (year,month,day,weekday,hours,minutes,seconds,subseconds)

print(time.localtime(1560350645))