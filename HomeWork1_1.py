my_duration = int(input('Please put your duration in sec:'))
duration_in_day = my_duration // 86400
duration_in_hours = (my_duration // 3600) % 24
duration_in_minutes = (my_duration // 60) % 60
duration_in_sec = my_duration % 60
if duration_in_day >= 1:
    print(f'{duration_in_day}, дн,  {duration_in_hours}, час, {duration_in_minutes}, мин, {duration_in_sec}, сек')
elif duration_in_hours >= 1:
    print(f'{duration_in_hours}, час, {duration_in_minutes}, мин, {duration_in_sec}, сек')
elif duration_in_minutes >= 1:
    print(f'{duration_in_minutes}, мин, {duration_in_sec}, сек')
else:
    print(f'{duration_in_sec}, сек')
