import datetime
import pandas as pd 

current_time = datetime.datetime.now()
current_time, current_minute = datetime.datetime.time(current_time).hour, datetime.datetime.time(current_time).minute
print('Current time:', current_time)
print('Current minute:', current_minute)
current_date = datetime.datetime.date(datetime.datetime.today())
print('Current date:', current_date)

agenda_worksheet = ''
agenda = pd.read_excel()
print(agenda)
