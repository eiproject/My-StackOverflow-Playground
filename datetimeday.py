from datetime import date
import datetime

# for day in range (1,365):
#     departure_date = date.today() + datetime.timedelta(days=day)

#     if departure_date.weekday() < 7:
#         day_of_week = departure_date.day
#     else:
#         day_of_week = departure_date.weekday()
#     print(day_of_week)

DAYS = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def week(start_day, days_in_month):
    start_day = start_day % 7
    print(' '.join(DAYS))
    month = []
    w = ['  ' for i in range(start_day-1)]
    for day in range(1, days_in_month+1):
        if day < 7 - start_day:
            w.append(f'{day % 7 - start_day + 1} ')
        else:
            w.append(f'{day % 7} ')
        if len(w) == 7:
            print(' '.join(w))
            month.append(w)
            w = []
    month.append(w)
    print(' '.join(w))
    print(month)

week(2, 31)