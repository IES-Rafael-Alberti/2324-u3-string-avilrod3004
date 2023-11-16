'''
Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
'''


def cuenta(palabra: str, letra_input: str):
    '''
    '''
    contador = 0
    for letra in palabra:
        if letra == letra_input:
            contador = contador + 1
    print(contador)


def main():
    palabra = input('Introduce una palabra: ')
    letra = input('Introduce una letra: ')

    num = cuenta(palabra, letra)


if __name__ == '__main__':
    main()