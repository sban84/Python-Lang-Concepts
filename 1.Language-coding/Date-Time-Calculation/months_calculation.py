"""Simple calculations on datetime module """
"""For simple calculation like overall time diff use just a_datetime - b_datetime 
But for cmplex calculations like add and delete dayes / months / hours etc 
use r = relativedelta(end_date, start_date)
and use r.API
as shown below 


NOTE : datetime.strftime(date_object , "str_frmat") -> to convert date to string 
datetime.strptime(date_object , "str_frmat") -> string to date object 
full list :- https://www.programiz.com/python-programming/datetime/strptime
"""

from datetime import  datetime
from dateutil.relativedelta import relativedelta

# months difference VERY IMP
curr_date_time = datetime.now()
another_date_time = datetime.strptime("2021-04-06 11:10:20.1232" , "%Y-%m-%d %H:%M:%S.%f")

r = relativedelta(curr_date_time , another_date_time)
months_diff_final = r.months + (r.years * 12)
print(f"months_diff_final "
      f"between {curr_date_time} and {another_date_time} is= {months_diff_final}")


# substract 36 months from now

cur_date = datetime.now()
sub_37_months = cur_date - relativedelta(months=37)
print("sub_37_months" , sub_37_months)


print("sub_37_months formatted in more readable " ,datetime.strftime(sub_37_months, "%Y-%m-%d %H:%M:%S"))

