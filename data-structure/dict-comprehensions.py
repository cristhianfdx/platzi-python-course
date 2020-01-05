if __name__ == '__main__':

    cuadrados = {}

    for num in range(1, 11):
        cuadrados[num] = num ** 2


    cuadrados2 = {num: num**2 for num in range(1, 11)}
