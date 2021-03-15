nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
number_of_jokes = int(input("Введите количество шуток, которое хотите получить:"))
flag = input("Если вы хотите только оригинальные (уникальные) шутки, то введите '1', иначе, то любое другое число:")


def get_jokes():
    for i in range(number_of_jokes):
        if flag == 1:
            from random import choice
            word_1 = choice(nouns)
            word_3 = choice(adjectives)
            word_2 = choice(adverbs)
            print(f'Ваша шутка:{word_1} {word_2} {word_3}')
        else:
            from random import choice
            word_1 = choice(nouns)
            nouns.remove(word_1)
            word_3 = choice(adjectives)
            adjectives.remove(word_3)
            word_2 = choice(adverbs)
            adverbs.remove(word_2)
            print(f'Ваша шутка:{word_1} {word_2} {word_3}')


get_jokes()
