students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
# print(students)
subjects = ', '.join(subjects)
# print(subjects)

text = f'Students {students} study these subjects: {subjects}'
print(text)
