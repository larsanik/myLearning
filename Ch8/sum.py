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
    nose = []
    tail = []
    for i in range(len(wrd)):
        nose.append(wrd[i])
        tail.append(wrd[-(i+1)])
    if tail == nose:
        return 'Полиндром'
    else:
        return 'Не полиндром'

def is_polindrom(word):
    i = 0
    j = len(word)-1
    while i<j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j -1
    return True

# sums = recursive_compute_sum(marbles)
# print('Сумма равна', sums)

wrd = 's'
print(check_polindrom(wrd))
print(is_polindrom(wrd))