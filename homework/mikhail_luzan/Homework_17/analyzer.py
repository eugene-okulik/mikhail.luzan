import argparse
import textwrap
import os

parser = argparse.ArgumentParser(
    prog='Logs analyzer',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
    Script for searching text in logs.
    ---------------------------------

    !!! Please make sure that
    the path to the logs folder is enclosed in quotes
    (e.g., "/path/to/folder") !!!
    ''')
)
parser.add_argument(
    'log_path',
    help='Full path to the folder where the log files are located. Always in quotes (e.g., "/path/to/folder")'
)
parser.add_argument('-t', '--text', required=True, help='What text do you need to find in the files?')
args = parser.parse_args()

log_path = args.log_path
text = args.text

if not os.path.isdir(log_path.strip('"')):
    print(f'Error: The specified path "{log_path}" does not exist')
    exit(1)

if not text.strip():
    print("Error: The search text cannot be empty")
    exit(1)


def show_line():
    words = line.split()
    index = words.index(text)
    start_word = max(0, index - 5)
    end_word = min(len(words), index + 5)
    result = ' '.join(words[start_word:end_word])

    print(f'Line: {result}')


def find_log_file():
    with os.scandir(log_path) as log_files:
        for obj in log_files:
            if obj.is_file() and obj.name.endswith('.log'):
                yield obj.path, obj.name


total_count = 0

for file_path, file_name in find_log_file():
    with open(file_path, encoding='utf-8') as log_file:
        for line_number, line in enumerate(log_file, start=1):
            if text in line:
                print(f'\nFile Name: {file_name}')
                print(f"Line's Number: {line_number}")
                show_line()
                total_count += 1
            continue

print(f'\nTotal number of matches ({text}): {total_count}')
