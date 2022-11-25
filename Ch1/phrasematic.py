import random
verbs =  ['Стремись','Нацеливайся','Держись в потоке','Не унывай',
          'Держи концентрацию','30 000 шагов','24/7','Побеждай'
          ,'Люби']

abjectives = ['Сильнее','Выше','Стойко','Стремительнее',
              'Собранно','Неудержимо','Стремительно','Суперски']

nouns = ['Процесс','Результат','Цель','Средства',
              'Высота','Достижения','Награда','Достоинство']

verb = random.choice(verbs)
abjective = random.choice(abjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + abjective + ' ' + noun

print(phrase)
