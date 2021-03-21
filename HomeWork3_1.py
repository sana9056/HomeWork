words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
         'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate():
    word = input("Введите слово от one до ten, чтобы перевести его на русский язык:")
    word.lower()
    print(f'Переводом слова: {word}, будет: {words.get(word)}')


num_translate()
