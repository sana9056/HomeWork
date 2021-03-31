import sys

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def name_gen():
    return (tuple([tutors[i]] + [klasses[i]]) for i in range(len(tutors)))


x = name_gen()
print(type(x), sys.getsizeof(x))
for j in range(len(tutors)):
    print(next(x))
