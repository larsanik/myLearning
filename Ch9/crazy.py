def make_crazy_lib(filename):
    file = open(filename, 'r', encoding="utf-8")

    text = ''

    for line in file:
        text = text + process_line(line)  # + '\n'

    file.close()

    return text


placeholders = ['ГЛАГОЛ', 'СУЩЕСТВИТЕЛЬНОЕ', 'ПРИЛАГАТЕЛЬНОЕ']


def process_line(line):
    processed_line = ''

    words = line.split()

    for word in words:
        if word in placeholders:
            answer = input('Введите ' + word + ": ")
            processed_line = processed_line + answer + ' '
        else:
            processed_line = processed_line + word + ' '
    return processed_line + '\n'


def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)


if __name__ == '__main__':
    main()
