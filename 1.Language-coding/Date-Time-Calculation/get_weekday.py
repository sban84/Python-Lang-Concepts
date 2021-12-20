from datetime import datetime
from dateutil.relativedelta import relativedelta

week_map = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday"}

inp = input("Enter a date ")
max_retry = 3
retry_count = 0
while (inp.lower() != "done") & (retry_count < max_retry):
    try:
        date = datetime.strptime(inp, "%d %m %Y")
        print(week_map.get(str(date.weekday())  ) )
        # and day of the week before 1 month
        one_month_before = date - relativedelta(months=1)
        print(f" date before one month of {date} is {one_month_before}")
        print(f"day of the week before one month of {date} is {week_map.get(str(one_month_before.weekday()))}")

    except ValueError as e:
        retry_count +=1
        print("Wrong input its need to be day month year format")
        print(f"you have {max_retry - retry_count} remaining , please try again!")
    inp = input("Enter a date ")


