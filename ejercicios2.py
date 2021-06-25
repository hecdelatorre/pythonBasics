# multiplicar dos números sin usar el símbolo de multiplicación

a = 5
b = 8
resultado = 0

for x in range(a):
    resultado+=b

print(f'{a} * {b} = {resultado}')

# ingresar nombre y apellido e imprimirlo al revez

nombre = 'Héctor'
apellido = 'De La Torre'

concatenacion = f'{nombre} {apellido}'
print(concatenacion[::-1])

# escrbir una función que encuentre el elemento menor de una lista


lista = [10, 20, 42, 44, 11, 32, 22, 13, 10, 4, 5, 2]
menor = 'init'

for x in lista:
    # print(x) 
    if menor == 'init':
        menor = x
    else:
        if x < menor:
            menor = x
        else:
            # menor = menor
            menor
        # menor = x if x < menor else menor
        # print(f' {menor}')

print(f'Numero menor {menor}')

# escrbir una función que encuentre el elemento mayor de una lista

mayor = 'init'

for x in lista:
    if mayor == 'init': mayor = x
    else: mayor = x if x > mayor else mayor

print(f'Numero mayor {mayor}')


# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calculaVolumen(r): return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)

# escribir una funcion que indique si un usuario es mayor de edad

def esMayor(usuario): return usuario.edad >= 18

class Usuario: 
    def __init__(self, edad): 
        self.edad = edad

usuario = Usuario(17)
usuario2 = Usuario(18)
usuario3 = Usuario(19)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)
resultado3 = esMayor(usuario3)

print(resultado1, resultado2, resultado3)

# escribir una función que indique si un número es par o impar

def esPar(n):
    return n % 2 == 0

resultado1 = esPar(10)
resultado2 = esPar(9)

print(resultado1, resultado2)

# escribir una función que indique cuantas vocales tiene una palabra

palabra = 'onomatopeya'
vocales = 0
for x in palabra:
    x = x.lower()
    vocales +=1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print(vocales)

# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados

lista = []
print('Ingrese numeros y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    if valor == 'basta': break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato invalido')
            exit()

resultado = 0
for x in lista: resultado += x
print(resultado)
