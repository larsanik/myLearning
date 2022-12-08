users = {}
users['Kim'] = {'email': 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}


def average_age(pers):
    frends_list = users[pers]['friends']
    summ_age = 0
    for i in frends_list:
        summ_age = summ_age + users[i]['age']
        aver_age = summ_age / len(frends_list)
    print(pers + ', средний возраст друзей:', aver_age)


average_age('Kim')
average_age('John')
average_age('Josh')
