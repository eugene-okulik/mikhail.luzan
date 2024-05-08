temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24,
    23
]

hot_days = list(filter(lambda x: x > 28, temperatures))

print(f'Hot days: {hot_days}')

max_t = max(hot_days)
min_t = min(hot_days)
avr_t = round(sum(hot_days) / len(hot_days), 1)

print(f'Max temperature is {max_t}')
print(f'Min temperature is {min_t}')
print(f'Average temperature is {avr_t}')
