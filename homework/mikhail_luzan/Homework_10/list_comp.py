PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split()

items = price_list[0::2]

prices = [int(x[:-1]) for x in price_list[1::2]]

new_dict = dict(zip(items, prices))

print(new_dict)
