
def is_palindrome2(word):
    reverse_word = word[::-1]
    return reverse_word == word


def is_palindrome(word):
    reverse_letters = []

    for letter in word:
        reverse_letters.insert(0, letter)

    reverse_word = ''.join(reverse_letters)

    return reverse_word == word

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    result = is_palindrome2(word)

    if result:
        print('{} si es un palindromo'.format(word))
    else:
        print('{} no es un palindromo'.format(word))