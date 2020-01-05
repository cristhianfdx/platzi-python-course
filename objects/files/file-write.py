'''
Con Python también podemos leer y escribir archivos del sistema.

Existen varios modos en los que podemos manejar archivos

‘r’ = leer
’w’ = escribir
’a’ = añadir
’r+’ = leer y escribir

Siempre recuerda cerrar el archivo.

El keyword with nos permite manejar el contexto al trabajar con archivos

'''

def run():
    with open('file-write.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))



if __name__ == '__main__':
    run()