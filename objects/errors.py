def divide(num1, num2):
    result = 0;

    try:
        result = num1 / num2
    except ZeroDivisionError:
        print('En caso de ocurrir un error')
    else:
        print('En caso de no ocurrir un error')
    finally:
        print('Se ejecuta si hay o no errores')


if __name__ == '__main__':
    divide(1, 4)