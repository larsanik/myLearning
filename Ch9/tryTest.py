try:
    num = input('Enter num: ')
    result = 42/int(num)
except ZeroDivisionError:
    print('Dont div on zero!')
except ValueError:
    print('Sorry, enter num please.')
else:
    print('Result: ', result)
finally:
    print('See You!')
