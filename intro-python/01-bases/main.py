# se puede "tipar los datos, pero no es restrictivo"
nombre: str = 'Juan'
edad = 3

# None, para declarar variables sin un valor inicial
apellido = None
esMayor = True

# formatedor de cadenas
print(f'Hola {nombre} ')

# función "len", obtiene el tamaño de un iterable
print(nombre[len(nombre) - 1])

# La función "list", permite crear una nueva lista con los calores enviados, o si es un string, caracter por caracter
print(list(nombre))

numeros = [1, 40, 19, 2, 3, 40, 4, 40, 40, 40]
# copia_numeros = numeros  # haciendo referencia al mismo valor en memoria
copia_numeros = numeros.copy() # hace una copia con una nueva referencia

numeros.sort()  # está mutando la variable orginal
numeros.pop()  # elimina el ultimo valor
numeros.pop(3)  # elimina el elemento en la posición 3
numeros.remove(40)  # elimina la primer coicidencia del "valor" enviado
numeros.append(100)  # agrega un valor al final
numeros.insert(0, 55)  # inserta un valor en la posición indicada

postres = ["galletas", "pie de limon", "dulce de leche"]
postres.sort()

print(postres)

print('original', numeros)
print('copia', copia_numeros)
