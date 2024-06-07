def numbers(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@numbers
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_num = float(input('Please enter the 1st number: '))
second_num = float(input('Please enter the 2nd number: '))

result = calc(first_num, second_num)
print('Result of the operation is', result)
