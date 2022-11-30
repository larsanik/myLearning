marbles = [10, 13, 39, 14, 41, 9, 3]


def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum = first + recursive_compute_sum(rest)
        return sum


def check_polindrom(wrd):
    if len(wrd) < 3:
        return 'Очень короткое слово!'
    else:
        return 'Похоже на слово!'


# sums = recursive_compute_sum(marbles)
# print('Сумма равна', sums)

wrd = 'sыыы'
print(check_polindrom(wrd))