def make_crazy_lib(filename):
    try:
        file = open(filename, 'r', encoding="utf-8")

        text = ''

        for line in file:
            text = text + process_line(line)  # + '\n'

        file.close()

        return text

    except FileNotFoundError:
        print("Not found file", filename + '.')
    except IsDirectoryError:
        print("Well", filename, '- this directory.')
    except:
        print("Not read file", filename)


placeholders = ['ГЛАГОЛ', 'СУЩЕСТВИТЕЛЬНОЕ', 'ПРИЛАГАТЕЛЬНОЕ']


def process_line(line):
    global placeholders
    processed_line = ''
    words = line.split()
    for word in words:
        stripped = word.strip('.,;?!')
        if stripped in placeholders:
            answer = input('Введите ' + word + ": ")
            processed_line = processed_line + answer + ' '
            if word[-1] in '.,;?!':
                processed_line = processed_line + word[-1] + ' '
        else:
            processed_line = processed_line + word + ' '
    return processed_line + '\n'


def save_crazy_lib(filename, text):
    file = open(filename, "w")

    file.write(text)
    file.close()


def main():
    filename = 'lib.txt'
    lib = make_crazy_lib(filename)
    if lib is not None:
        save_crazy_lib('crazy_' + filename, lib)


if __name__ == '__main__':
    main()
