import pandas as pd
import datetime
from dateutil.parser import parse

time=parse("2011-01-03")
print(str(time))

time=parse("Jan 31,1997 10:45 PM")
print(str(time))