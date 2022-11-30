def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        first = word[0]
        last = word[-1]
        middle = word[1:-1]
        if first == last:
            return is_palindrome(middle)
        else:
            return False


words = ['tacocat', 'radar', 'yak', 'rader', 'kaujak']
for word in words:
    print(word, is_palindrome(word))