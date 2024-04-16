numb = 15

while True:
    user_input = int(input('Please guess the number: '))
    if user_input == numb:
        break
    else:
        print('Try again')
print("Congrats! You're right")
