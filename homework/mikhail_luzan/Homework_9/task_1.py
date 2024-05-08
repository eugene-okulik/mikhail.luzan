import datetime

date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')

month = python_date.strftime('%B')
print(f'Month is {month}')

new_format = python_date.strftime('%d.%m.%Y, %H:%M')
print(f'New data format is "{new_format}"')
