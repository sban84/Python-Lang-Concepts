from datetime import datetime
from dateutil.relativedelta import relativedelta

start = "2021-04-06"
end = "2021-05-02"

def months_diff(end,start):
    start = datetime.strptime(start,"%Y-%m-%d")
    end = datetime.strptime(end,"%Y-%m-%d")
    r = relativedelta(end,start)
    months = r.months
    print(months)
    return months


print(f"months_diff_final "
f"between {start} and {end} is= {months_diff(end,start)}")
