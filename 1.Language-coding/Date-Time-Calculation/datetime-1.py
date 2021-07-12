"""Simple calculations on datetime module """
"""For simple calculation like overall time diff use just a_datetime - b_datetime 
But for cmplex calculations like add and delete dayes / months / hours etc 
use r = relativedelta(end_date, start_date)
and use r.API
as shown below 
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

curr_date_time = datetime.now()
print(f"curr_date_time {curr_date_time}")
#datetime.today()

another_date_time = datetime.strptime("2021-04-06 11:10:20.1232" , "%Y-%m-%d %H:%M:%S.%f")
print(another_date_time)

time_delta = curr_date_time - another_date_time

print("time_delta",time_delta)

# get more control on the difference , add , minus etc
n = 40
curr_date_time_added_n_days = curr_date_time + relativedelta(days=n)
print("curr_date_time_added_n_days", curr_date_time_added_n_days)
curr_date_time_added_n_days_fmted = datetime.strftime(curr_date_time_added_n_days,"%d %B %Y")
print("curr_date_time_added_n_days_fmted" , curr_date_time_added_n_days_fmted)

import pytz
berlin_time = curr_date_time_added_n_days.astimezone(tz=pytz.timezone("Europe/Berlin"))
print("berlin_time",berlin_time)

india_time= curr_date_time_added_n_days.astimezone(tz=pytz.timezone("Asia/Kolkata"))
print("india_time",india_time)










