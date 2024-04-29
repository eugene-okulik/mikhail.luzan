import sys

sys.set_int_max_str_digits(100000)


def fibonacci(limit=100):
    num_1 = 0
    num_2 = 1
    while num_1 < limit:
        yield num_1
        num_2 += num_1
        num_1 = num_2 - num_1


grade = 1
counts = [5, 200, 1000, 100000]
for count in counts:
    for result in fibonacci(10**100000):
        if grade == count:
            print(f'The number #{count} is {result}')
            break
        else:
            grade += 1
