operation_result_1 = 'результат операции: 42'
operation_result_2 = 'результат операции: 514'
program_result = 'результат работы программы: 9'

index_1 = operation_result_1.index('42')
# print(index_1)
index_2 = operation_result_2.index('514')
# print(index_2)
index_3 = program_result.index('9')
# print(index_3)

get_number_1 = int(operation_result_1[index_1:])
# print(get_number_1)
get_number_2 = int(operation_result_2[index_2:])
# print(get_number_2)
get_number_3 = int(program_result[index_3:])
# print(get_number_3)
addition_number = 10

sum_1 = get_number_1 + addition_number
sum_2 = get_number_2 + addition_number
sum_3 = get_number_3 + addition_number

print('Sum of the 1st number:', sum_1)
print('Sum of the 2nd number:', sum_2)
print('Sum of the 3rd number:', sum_3)
