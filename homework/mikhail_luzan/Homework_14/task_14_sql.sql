-- Complete set of information about the student --

select * from students

insert into students 
(name, second_name, group_id)
values ('Mike', 'Jordan', NULL)

select * from students
where name = 'Mike' AND second_name = 'Jordan'

select * from books

insert into books 
(title, taken_by_student_id)
values 
('Fourth Wing', 1662),
('The Future', 1662),
('Hell Bent', 1662)

select * from books
where taken_by_student_id = 1662

select * from `groups`

insert into `groups` 
(title, start_date, end_date)
values
('Fantasy', '2024-07-28 00:00:00.000', '2024-08-28 00:00:00.000')

select * from `groups`
where title = 'Fantasy'

update students 
set group_id = 1598
where id = 1662

select * from students
where name = 'Mike' AND second_name = 'Jordan'

select * from subjets

insert into subjets 
(title)
values
('Algebra'),
('Geometry'),
('Belarusian Literature')

select * from subjets 
order by id DESC

select * from lessons

insert into lessons 
(title, subject_id)
values
('Onboarding',2130),
('Main',2130),
('Onboarding',2131),
('Main',2131),
('Onboarding',2132),
('Main',2132)

select * from lessons
where subject_id IN (2130, 2131, 2132)

select * from marks

insert into marks 
(value, lesson_id, student_id)
values
(8, 4722, 1662),
(9, 4723, 1662),
(7, 4724, 1662),
(9, 4725, 1662),
(7, 4726, 1662),
(8, 4727, 1662)

select * from marks
where student_id = 1662

-- Get information from the database --

-- 1. All student's grades:

select * from marks
where student_id = 1662

-- 2. All books in the student's possession:

select * from books
where taken_by_student_id = 1662

-- 3. All information about the student:
-- s.name as "First Name", s.second_name as "Last Name", g.title as "Group", b.title as "Book", s2.title as "Subject", l.title as "Lesson", m.value as "Mark"

select s.name as "First Name", s.second_name as "Last Name", g.title as "Group", b.title as "Book", s2.title as "Subject", l.title as "Lesson", m.value as "Mark" from students s 
left join `groups` g on g.id = s.group_id
left join books b on b.taken_by_student_id = s.id
left join marks m on m.student_id = s.id
left join lessons l on l.id = m.lesson_id
left join subjets s2 on s2.id = l.subject_id 
where s.id = 1662
