# mapas, objeos o json (clave/valor)

persona = {
    'nombre': 'Juan',
    'edad': 30,
    'direccion': {
        'lat': 124.344,
        'lng': 443.234
    }
}

persona2 = dict({
    'nombre': 'Juan',
    'edad': 30,
    'direccion': {
        'lat': 124.344,
        'lng': 443.234
    }
})

persona2['apellido'] = 'Alvarenga'

persona.pop('direccion')  # elimina una propiedad del diccionario
persona.copy()# Realiza una copia del diccionario

print(persona)
print(persona2)
print(persona['nombre'])
print(persona.get('edad'))


print(persona.keys()) # un listado con las claves del diccioanrio
print(persona.items()) # un listado de tuplas

for key in persona2:
    print(persona2[key])


# for key,value in persona2.items():
#     print(value)