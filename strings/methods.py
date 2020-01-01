
def run():
    name = 'Cristhian'
    name2 = name + ' Alexander'
    list2 = ['c', 'r', 'a', 's', 'h']

    print(name)
    print('')
    print('upper -> {}'.format(str_upper(name)))
    print('isupper -> {}'.format(str_is_upper(name)))

    print('lower -> {}'.format(str_lower(name)))
    print('islower -> {}'.format(str_is_lower(name)))

    print('find ->  <r> se encuentra en la posición: {}'.format(str_find(name, 'r')))

    print('length ->  la longitud es: {}'.format(str_len(name)))

    print('isdigit -> {}'.format(str_is_digit(name)))

    print('endswith -> {}'.format(str_endswith(name, 'n')))

    print('startswith -> {}'.format(str_startswith(name, 'C')))

    print('split -> {}'.format(str_split(name2)))

    print('join -> {}'.format(str_join(list2)))



def str_upper(string):
    return string.upper()

def str_is_upper(string):
    return string.isupper()

def str_lower(string):
    return string.lower()

def str_is_lower(string):
    return string.islower()

def str_find(string, letter):
    return string.find(letter)

def str_len(string):
    return len(string)

def str_is_digit(string):
    return string.isdigit()

def str_endswith(string, letter):
    return string.endswith(letter)

def str_startswith(string, letter):
    return string.startswith(letter)

def str_split(string):
    return string.split(' ')

def str_join(list):
    return ''.join(list)

if __name__ == '__main__':
    run()