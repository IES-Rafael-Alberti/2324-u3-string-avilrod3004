'''
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
'''

def pedir_palabra():
    '''
    '''
    palabra = input('Introduce una cadena de texto: ')

    return palabra


def main():
    palabra = pedir_palabra()

    num = len(palabra) - 1

    cont = 0
    while cont <= num:
        print(palabra[num - cont])
        cont += 1


if __name__ == '__main__':
    main()