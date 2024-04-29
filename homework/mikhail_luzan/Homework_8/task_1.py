import random


salary = int(input('Please enter your salary: '))
bonus = bool(random.randrange(0, 2))

if bonus is True:
    add_bonus = random.randrange(1, salary)
    total_salary = salary + add_bonus
else:
    add_bonus = 0
    total_salary = salary

print(f'Default salary = ${salary}, {bonus}, Bonus = ${add_bonus} --> Total salary = ${total_salary}')
