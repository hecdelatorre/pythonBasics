def miFuncion():
  print('Mi primera función')
# miFuncion()

def imprimeDato(arumento1):
  print(f'Mi argumento es: {arumento1}')

# imprimeDato('Parametro 1')

def imprimeNombre(nombre, apellido):
    print(f'El nombre completo es: {nombre} {apellido}')

# imprimeNombre('Héctor', 'De La Torre')

def imprimeCosas(*cosas):
    print('Los datos son: ', cosas)
    print('Los datos son: ', cosas[0])

# imprimeCosas('Chanchito', 'Feliz', 'lala', 'rolo')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre='Chanchito', apellido='Feliz')

def nombreCompleto2(**kgargs):
    print(kgargs['nombre'], kgargs['apellido'])

# nombreCompleto2(nombre='Chanchito', apellido='Feliz')

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)
 
# miFuncion2()
# miFuncion2('Batman')

def miFuncionLista(lista):
    for el in lista: print(el)

# miFuncionLista(['Chanchito', 'Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista: 
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Felipe'])
# print(nombres)

def recurcion(i):
    if(i < 1):
        return i
    print(i)
    recurcion(i - 1)

recurcion(6)

lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def printList(myList):
    for ml in myList:
        print(f' {ml}')
    print()

printList(lista)
