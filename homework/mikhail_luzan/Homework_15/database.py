import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

student = '''
insert into students
(name, second_name, group_id)
values (%s, %s, %s)
'''
cursor.execute(student, ('Mike', 'Jordan', None))

student_id = cursor.lastrowid

query = "select * from students where id =  %s"
cursor.execute(query, (student_id,))
data = cursor.fetchone()

student_name = f'{data["name"]} {data["second_name"]}'

print(f'\nStudent:\n{data}')

book = '''
insert into books
(title, taken_by_student_id)
values (%s, %s)
'''
cursor.executemany(
    book,
    [
        ('Fourth Wing', student_id),
        ('The Future', student_id),
        ('Hell Bent', student_id)
    ]
)

query = "select * from books where taken_by_student_id = %s"
cursor.execute(query, (student_id,))
data = cursor.fetchall()

print('\nBooks:')
for row in data:
    print(row)

group = '''
insert into `groups`
(title, start_date, end_date)
values (%s, %s, %s)
'''
cursor.execute(group, ('Fantasy', '2024-07-28 00:00:00.000', '2024-08-28 00:00:00.000'))

group_id = cursor.lastrowid

query = "select * from `groups` where id = %s"
cursor.execute(query, (group_id,))
data = cursor.fetchone()

print(f'\nGroup:\n{data}')

student_upd = '''
update students
set group_id = %s
where id = %s
'''
cursor.execute(student_upd, (group_id, student_id))

query = "select * from students where id = %s"
cursor.execute(query, (student_id,))
data = cursor.fetchone()

print(f'\nStudent updated:\n{data}')

subject = '''
insert into subjets
(title)
values (%s)
'''
subjects_created = ['Algebra', 'Geometry', 'Belarusian Literature']
sub_ids = []

for x in subjects_created:
    cursor.execute(subject, (x,))
    subject_id = cursor.lastrowid
    sub_ids.append(subject_id)

placeholders = ', '.join(['%s'] * len(sub_ids))  # A string of placeholders is created for the SQL IN clause (%s, %s ..)
query = f'select * from subjets where id IN ({placeholders})'
cursor.execute(query, sub_ids)  # sub_ids = (sub_ids[0], sub_ids[1] ..)
data = (cursor.fetchall())

print('\nSubjects:')
for row in data:
    print(row)

lesson = '''
insert into lessons
(title, subject_id)
values (%s, %s)
'''
lessons_created = ['Onboarding', 'Main']
les_ids = []

for sub_id in sub_ids:
    for x in lessons_created:
        cursor.execute(lesson, (x, sub_id))
        lesson_id = cursor.lastrowid
        les_ids.append(lesson_id)

query = f'select * from lessons where subject_id IN ({placeholders})'  # see the subject creation code above
cursor.execute(query, sub_ids)
data = cursor.fetchall()

print('\nLessons:')
for row in data:
    print(row)

mark = '''
insert into marks
(value, lesson_id, student_id)
values (%s, %s, %s)
'''

for les_id in les_ids:
    cursor.execute(
        mark,
        (
            input(f'\nGive a mark (0-10) for the {student_name} for the Lesson {les_id}: '), les_id, student_id
        )
    )

query = "select * from marks where student_id = %s"
cursor.execute(query, (student_id,))
data = cursor.fetchall()

print('\nMarks:')
for row in data:
    print(row)

student_info = '''
select s.name as "First Name", s.second_name as "Last Name", g.title as "Group", b.title as "Book",
s2.title as "Subject", l.title as "Lesson", m.value as "Mark" from students s
left join `groups` g on g.id = s.group_id
left join books b on b.taken_by_student_id = s.id
left join marks m on m.student_id = s.id
left join lessons l on l.id = m.lesson_id
left join subjets s2 on s2.id = l.subject_id
where s.id = %s
'''
cursor.execute(student_info, (student_id,))
data = cursor.fetchall()

print('\nStudent Info:')
for row in data:
    print(row)

db.commit()

db.close()
