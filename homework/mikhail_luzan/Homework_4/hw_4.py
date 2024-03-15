my_dict = {}
my_dict['tuple'] = (5, 9, 'text', True, 3)
my_dict['list'] = ['first', 159, None, 753, 'last']
my_dict['dict'] = {'first': '1234', 'second': '987654', 'third': '1', 'fourth': '25836', 'fifth': '458'}
my_dict['set'] = {'text', 34, False, 55.55, True}

print("The last element of 'tuple' key:", my_dict['tuple'][-1])

my_dict['list'].append(1544)
my_dict['list'].pop(1)

my_dict['dict']['dict_tuple'] = ('i am a tuple', 'element 2', 'element 3')
my_dict['dict'].pop('fifth')

my_dict['set'].add('new')
my_dict['set'].remove(False)

print("Updated dictionary:", my_dict)
