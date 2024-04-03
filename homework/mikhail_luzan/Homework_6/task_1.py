text = (
        'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' +
        ' dignissim vitae libero'
)
words = text.split()
final_text = []
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
    else:
        word = word + "ing"
    final_text.append(word)
print(' '.join(final_text))
