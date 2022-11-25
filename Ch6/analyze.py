#import ch1text


def count_syllables_in_word(word):
    count = 0

    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count = count + 1

    return count


def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count


def count_sentences(text):
    count = 0

    for char in text:
        terminals = '.!?'
        if char in terminals:
            count = count + 1

    return count

def output_results(score):
    if score >= 90:
        print('Уровень 5-го класса')
    elif score >= 80:
        print('Уровень 6-го класса')
    elif score >= 70:
        print('Уровень 7-го класса')
    elif score >= 60:
        print('Уровень 8-9-го классов')
    elif score >= 50:
        print('Уровень 10-11-го классов')
    elif score >= 30:
        print('Уровень студента ВУЗ-а')
    else:
        print('Уровень выпускника ВУЗ-а')

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllaЬles = count_syllables(words)

    score = (206.835-1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllaЬles/total_words))

    #print(total_words, 'слов')
    #rint(total_sentences, 'предложений')
    #print(total_syllaЬles, 'слогов')
    #rint(score, ' - удобочитаемость')
    output_results(score)


if __name__ == '__main__':
    import ch1text
    print('Текст главы 1:')
    compute_readability(ch1text.text)
