if __name__ == '__main__':

    pares1 = []
    for num in range(1, 31):
        if num % 2 == 0:
            pares1.append(num)


    pares2 = [num for num in range(1, 31) if num % 2 == 0]
