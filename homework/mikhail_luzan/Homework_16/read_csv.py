import os
import csv
import dotenv
import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(data_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    csv_data = []
    for row in file_data:
        csv_data.append(row)

print('\nCSV data: ')
for row in csv_data:
    print(row)

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

query = '''
select s.name, s.second_name, g.title as "group_title", b.title as "book_title",
s2.title as "subject_title", l.title as "lesson_title", m.value as "mark_value" from students s
left join `groups` g on g.id = s.group_id
left join books b on b.taken_by_student_id = s.id
left join marks m on m.student_id = s.id
left join lessons l on l.id = m.lesson_id
left join subjets s2 on s2.id = l.subject_id
'''
cursor.execute(query)
db_data = cursor.fetchall()

no_match = list(filter(lambda x: x not in db_data, csv_data))
print('\nData mismatch between CSV & DB (data not in DB): ')
for row in no_match:
    print(row)

db.close()
