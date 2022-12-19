users = {'Kim': {'email': 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['John', 'Josh']},
         'John': {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']},
         'Josh': {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}}

max = 1000
for name in users:
    user = users[name]
    frends = user['friends']
    if len(frends) < max:
        most_anti_social = name
        max = len(frends)

print('Меньше всего друзей имеет', most_anti_social)