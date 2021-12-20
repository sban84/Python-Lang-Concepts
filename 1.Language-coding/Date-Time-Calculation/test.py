from datetime import datetime

import dateutil.relativedelta

d = datetime.strptime("2 08 2021", "%d %m %Y")
print(d)
print(d.weekday())
