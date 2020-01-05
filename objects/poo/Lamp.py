class Lamp:
    __LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self.__is_turned_on = is_turned_on


    def turn_on(self):
        self.__is_turned_on = True
        self.__display_image()


    def turn_off(self):
        self.__is_turned_on = False
        self.__display_image()


    def __display_image(self):
        if self.__is_turned_on:
            print(self.__LAMPS[0])
        else:
            print(self.__LAMPS[1])



def run():
    lamp = Lamp(is_turned_on=True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir

        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()





