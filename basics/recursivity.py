
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)


if __name__ == '__main__':
    number = int(input('Ingrese número: '))
    result = factorial(number)
    print('')
    print('El factorial de {} es: {}'.format(number, result))