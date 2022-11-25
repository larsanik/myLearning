greeting = 'Hello'
test_none = None


def greet(name, emoticon, message='All cool!'):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '!', message, emoticon)


greet('Jun', '=o)', 'See you!')
greet('Boss', '=o)')
greet(message='Who is!?', name='Elis', emoticon='>_<')
print(greeting)
print(test_none)
print(type(test_none))
