import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(data_path, encoding='utf-8') as data_file:
    data = data_file.read()
    print(f'\nFile data: \n{data}')


def read_file():
    with open(data_path, encoding='utf-8') as data_file2:
        for line in data_file2.readlines():
            yield line


for date_line in read_file():
    dot_index = date_line.index(".")
    dash_index = date_line.index(" - ")

    date_str = date_line[dot_index + 2:dash_index]
    python_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    line_number = int(date_line[:dot_index])

    if line_number == 1:
        new_date = python_date + datetime.timedelta(weeks=-1)
        print(f'\nThe date is a week later ({python_date}): {new_date}')
    elif line_number == 2:
        week_day = python_date.strftime("%A")
        print(f'\nDay of the week ({python_date}): {week_day}')
    elif line_number == 3:
        now = datetime.datetime.now()
        time_delta = (now - python_date).days
        print(f'\nHow many days ago that date ({python_date}) was: {time_delta} day(s)')
    else:
        print(f'\nDate: {python_date}')
