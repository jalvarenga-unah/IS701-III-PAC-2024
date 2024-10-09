# Todas las funciones retornan por dafault "None"

def saludo():
    print('Hola mundo desde una función')
    print('Este mensaje, tambien fué enviado desde la función')
    return 3

def sumaNumeros(*nums):
    return sum(nums)

def crearDict(**params):
    print(params)

def suma(n1, n2):
    return n1 + n2  # es la ultima instrucción dentro de la función
    print('dwefewf')  # nunca llega


def division(n1, n2):
    return n1 / n2


def saludar(nombre='Mundo'):
    print(f"Hola {nombre}")

if __name__ == "__main__":

    print('Este mensaje, fué enviado desde fuera la función')

    saludo()  # ejecutar la función

    otraFuncion = saludo  # obteniendo la referencia en memoria de "saludo"

    print(otraFuncion())

    print(suma(n1=2, n2=3))
    print(division(n2=2, n1=0))
    saludar(nombre="Enrique")

    print(max([1, 4, 5, 8, 90]))
    print(max(1, 4, 444, 5, 8, 90))
    print(max(['a', 'b', 'c']))

    print(sumaNumeros(1, 5, 4, 23, 6))

    crearDict(a=3, b=4, c=5, d=6)
