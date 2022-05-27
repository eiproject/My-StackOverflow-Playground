from datetime import date, datetime
import pandas as pd

df = pd.read_csv("date.csv", parse_dates = ["dates"])

#a date to substact dates in csv
defined_date = pd.to_datetime(date(2020,12,25))

#a list of dates from a csv file
csv_dates = df.dates

# diff = [defined_date  - csv_dates[0].date()]
diff = [defined_date  - csv_dates]
print(diff)