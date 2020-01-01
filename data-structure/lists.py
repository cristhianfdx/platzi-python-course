# -*- coding=utf-8 -*-

# Una lista es una secuencia de elementos, para crearlas usamos corchetes [] o con la función list

# names = ['Cristhian', 'Maria', 'Luis', 'Camila', 'Pedro']

# lastnames = list()
# lastnames.append('Forero')
# lastnames.append('Lopez')
## lastnames = ['Forero', 'Lopez']

def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temps(temps)

    print('La temperatura promedio es {}'.format(average))
