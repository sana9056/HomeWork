words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
         'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv():
    word = input("Введите слово от one до ten, чтобы перевести его на русский язык:")
    word_test = str(word)
    word = word.lower()
    if word_test.istitle():
        b = str(words.get(word))
        print(f'Переводом слова: {word.title()}, будет: {b.title()}')
    else:
        print(f'Переводом слова: {word}, будет: {words.get(word)}')


num_translate_adv()
