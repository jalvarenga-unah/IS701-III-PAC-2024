import numpy as np


lista1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# lista2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# lista3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(lista1d.shape)
# print(lista2d.shape)
# print(lista3d.shape)

print(lista1d.size)  # equivalente a len(lista1d)

lista1d.mean()  # promedio de la lista
lista1d.max()  # máximo de la lista
lista1d.min()  # mínimo de la lista

# slicing

# considera los elementos desde el índice
# 2 hasta el 5, sin incluir el 5
print(lista1d[2: 5])
print(lista1d[5:])  # considera los elementos desde el índice 5 hasta el final
print(lista1d[2])  # acceder al elemento en la posición 2
print(lista1d[::-1])  # invertir la lista

# concatenar listas
lista1 = np.array([1, 2, 3])
lista2 = np.array([4, 5, 6])

lista3 = np.dot(lista1, lista2) # producto punto