'''
Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano

y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.
'''

def main():
    palabra = input('Introduce una palabra: ')
    letra = input('Introduce una letra: ')

    num = palabra.count(letra)

    print(f'La letra {letra} aparece {num} veces')


if __name__ == '__main__':
    main()