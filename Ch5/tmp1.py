a = 20  # определены вне функции
b = 10
glass = 'полный'

def drink_me(param, glass) :
    msq = 'Выпиваем ' + param + ' стакан' + glass
    print(msq)
    param = 'пустой'

def sum():
    global a
    b = 15
    c = a + b  # Использование глобальных переменных
    print("Сумма:", c)
    b = 20



drink_me(glass, ' перекрытие')
print ('Стакан', glass)

sum()