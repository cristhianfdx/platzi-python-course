i = 0
while i <= 5:
    print(i)
    i += 1

# 0
# 1
# 2
# 3
# 4
# 5

import random


def run():
    found = False
    random_number = random.randint(0, 20)

    while not found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('El número {} fue encontrado'.format(number))
            found = True
        elif number > random_number:
            print('El número es mas pequeño')
        else:
            print('El número es mas grande')


if __name__ == '__main__':
    run()

