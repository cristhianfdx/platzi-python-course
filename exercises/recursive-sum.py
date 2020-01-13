def sum(num):
    if num == 1:
        return num
    elif num > 1:
        s = num + sum(num -1)

    return s


if __name__ == '__main__':
    num = int(input('Ingrese un número: '))

    result = sum(num)

    print('La suma de 1 hasta {} es: {}'.format(num, result))
