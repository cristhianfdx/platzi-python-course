countries = {
    'mexico': 122,
    'colombia': 49,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Escribe el nombre de un pais: ')).lower()
    try:
        print('La población de {} es de {} millones'.format(country, countries[country]))
    except KeyError:
        print('No se encuentra el dato del país solicitado')


