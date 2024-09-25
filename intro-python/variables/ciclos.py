rango = range(1,10, 2) # que va desde el 1 hasta el 10, sin incluir el 10

for valor in rango:
    print(valor)
print('fuera del ciclo') # finalizó el ciclo for

postres = ["galletas", "pie de limon", "dulce de leche"]

tupla = tuple(postres)

print(tupla)

# enumerate: generea una lista de tuplas que contiene los indices
# de cada valor del iterable
for index,postre in enumerate(postres):
    print(index,postre)

nombre = 'Juan Alvarenga'

for letra in nombre:
    print(letra)