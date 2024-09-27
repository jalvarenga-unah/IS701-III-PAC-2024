

edad = 10

if not edad > 18:
    print('Es mayor de edad')
    print('sigue dentro de la condición verdadera') 
elif edad <= 60:
    print('Es adulto')
    print('sigue dentro de la condición verdadera')
else:
    print('Es menor de edad')
    print('sigue dentro de la condición falsa')

nombre = 'Juan'

if 'h' in nombre:
    print('La letra h está en el nombre')

estadoCivil = 'soltero'

# nuevo switch case
match estadoCivil:
    case 'soltero':
        print('Aproveche la vida hermano')
    case 'casado':
        print('Felicidades (cof cof) :$')
    case 'divorciado':
        print('A seguir adelante')


dictEstadoCivil = {
    'soltero': 'Aproveche la vida hermano',
    'casado': 'Felicidades (cof cof) :$',
    'divorciado': 'A seguir adelante'
}

print(dictEstadoCivil[estadoCivil])