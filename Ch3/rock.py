# Импорт библиотеки
import random

# Инициализация переменной для победителя
winner = ''

# Выбор компьютера
random_choice = random.randint(0, 2)

# Сопоставление выбора компьютера словам
if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'ножницы'
else:
    computer_choice = 'бумага'

# Запрос выбора пользователя
user_choice = ''
while (user_choice != 'камень' and
       user_choice != 'ножницы' and
       user_choice != 'бумага'):
    user_choice = input('камень, ножницы или бумага? -> ')

# Алгоритм оперделения победителя
if computer_choice == user_choice:
    winner = 'Ничья'
elif computer_choice == 'бумага' and user_choice == 'камень':
    winner = 'Компьютер'
elif computer_choice == 'камень' and user_choice == 'ножницы':
    winner = 'Компьютер'
elif computer_choice == 'ножницы' and user_choice == 'бумага':
    winner = 'Компьютер'
else:
    winner = 'Пользователь'

# Подведение тиогов игры
if winner == 'Ничья':
    print('Мы оба выбрали', computer_choice + ', играем снова =о).')
else:
    print(winner, 'выиграл, я выбрал', computer_choice + '.')
