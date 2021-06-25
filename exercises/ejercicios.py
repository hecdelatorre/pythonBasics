# dato = input('Ingrese dato: ')
# lista = ['hola', 'mundo', 'chanchito', 'feliz']
# for li in lista: print(li)
# if lista.count(dato) > 0: print(f'El dato {dato} existe')
# else: print(f'El dato {dato} no existe {dato}') 


primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingreso segundo número: ')

try: segundo = int(segundo)
except: segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('Ingrese operacion: ')

if simbolo == '+': print('Suma', primero + segundo)
elif simbolo == '-': print('Resta', primero - segundo)
elif simbolo == '*': print('Multiplicación', primero * segundo)
elif simbolo == '/': print('Divición', primero / segundo)
else: print('El simbolo ingresado no es valido')

# if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
#     print('Ingresaste mal un dato, prueba de nuevo solo con números')
# else:
#     print(primero + segundo)
