string_1 = 'результат операции: 42'
string_2 = 'результат операции: 54'
string_3 = 'результат работы программы: 209'
string_4 = 'результат: 2'
addition_number = 10


def summ(string):
    numb = int(string.split()[-1])
    return numb + addition_number


print(summ(string_1))
print(summ(string_2))
print(summ(string_3))
print(summ(string_4))
