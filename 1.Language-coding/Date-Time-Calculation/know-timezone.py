# Time conversion from local time
import datetime
import pytz

dt_today = datetime.datetime.today()  # Local time

print(f"dt_today from datetime.datetime.today()= {datetime.datetime.today()}")  # 2021-06-24 16:06:13.436779

dt_India = dt_today.astimezone(pytz.timezone('Asia/Kolkata'))
print("dt_India", dt_India)  # 2021-06-24 19:36:13.436750+05:30
dt_London = dt_today.astimezone(pytz.timezone('Europe/London'))
print("dt_London", dt_London)

# Format the times in custom way strftime convert datetime to str
# and strptime converts str to datetime object.
India = (dt_India.strftime('%m/%d/%Y %H:%M'))
London = (dt_London.strftime('%m/%d/%Y %H:%M'))
print("Indian standard time: " + India + " IST")
print("British Summer Time: " + London + " BST")


def get_all_timezone():
    import pytz
    for tz in pytz.all_timezones:
        print(tz)

# get_all_timezone()
