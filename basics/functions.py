# -*- coding=utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dummy = turtle.Turtle()
    make_square(dummy)
    turtle.mainloop()


def make_square(dummy):
    length = int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line(dummy, length)


def make_line(dummy, length):
    dummy.forward(length)
    dummy.left(90)


if __name__ == '__main__':
    main()
