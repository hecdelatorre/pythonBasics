# escribir una función que reciba nombre y apellido y los vaya agregando a un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombreCompleto.txt', 'a')
    c.write(f'{nombre} {apellido}\n')
    c.close()

agregaNombreAArchivo('Hector', 'De La Torre')
