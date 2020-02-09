from tkinter import *
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run():
    main = Tk()
    main.title('Test window')


    if (sys.platform.startswith('win')):
        main.iconbitmap(os.path.join(BASE_DIR, 'favicon.ico'))
    else:
        logo = PhotoImage(file=os.path.join(BASE_DIR, 'favicon.png'))
        main.tk.call('wm', 'iconphoto', main._w, logo)

    main.geometry('650x350')
    main.config(bg='blue')
    main.mainloop()

if __name__ == '__main__':
    run()