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

print(f'\nBooks:')
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
cursor.executemany(
    subject,
    [
        ('Algebra',),
        ('Geometry',),
        ('Belarusian Literature',)
    ]
)

query = "select * from subjets order by id DESC limit %s"
cursor.execute(query, (3,))
data = (cursor.fetchall())
data_reversed = data[::-1]

ids = list(map(lambda item: item['id'], data_reversed))

print(f'\nSubjects:')
for row in data_reversed:
    print(row)

lesson = '''
insert into lessons
(title, subject_id)
values (%s, %s)
'''
cursor.executemany(
    lesson,
    [
        ('Onboarding', ids[0]),
        ('Main', ids[0]),
        ('Onboarding', ids[1]),
        ('Main', ids[1]),
        ('Onboarding', ids[2]),
        ('Main', ids[2])
    ]
)

query = "select * from lessons where subject_id IN (%s, %s, %s)"
cursor.execute(query, (ids[0], ids[1], ids[2]))
data = cursor.fetchall()

ids = list(map(lambda item: item['id'], data))

print(f'\nLessons:')
for row in data:
    print(row)

mark = '''
insert into marks
(value, lesson_id, student_id)
values (%s, %s, %s)
'''
cursor.executemany(
    mark,
    [
        (8, ids[0], student_id),
        (9, ids[1], student_id),
        (7, ids[2], student_id),
        (9, ids[3], student_id),
        (7, ids[4], student_id),
        (8, ids[5], student_id)
    ]
)

query = "select * from marks where student_id = %s"
cursor.execute(query, (student_id,))
data = cursor.fetchall()

print(f'\nMarks:')
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

print(f'\nStudent Info:')
for row in data:
    print(row)

db.commit()

db.close()
