def bark(name, weight):
    if weight > 20:
        print(name, 'говорит ГАВ-ГАВ')
    else:
        print(name, 'говорит гав-гав')


def prop_pers(question, answer):
    tmp = question + " [" + answer + "]?"
    prop = input(tmp)
    if prop == '':
        prop = answer
    print('Вы выбрали', prop)


bark('Тузик', 40)
bark('Смайли', 9)
bark('Джексон', 12)
bark('Филя', 65)

prop_pers('Цвет волос', 'темные')
