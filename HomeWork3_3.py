names = {}


def thesaurus(*args):
    for i in range(len(args)):
        word = args[i]
        if word[0] in names.keys():
            names[word[0]] = names[word[0]] + [word]
        else:
            names[word[0]] = [word]
    print(names)


thesaurus("Иван", "Мария", "Петр", "Илья")
