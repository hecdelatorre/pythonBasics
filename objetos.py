# class Usuario:
#     nombre = "Felipe"
#     apellido = 'Feliz'

# usuario = Usuario()
# usuario2 = Usuario()

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print(f'Hola me llamo {self.nombre} y soy administrador')

# usuario = Usuario('Felipe', 'Feliz')
# usuario2 = Usuario('Chanchito', 'Feliz')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# usuario.saludo()
# usuario2.saludo()

# usuario.nombre = 'Chanchito'
# usuario.saludo()

# del usuario.nombre
# usuario.saludo()
# del usuario
# print(usuario)

# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print(f'Hola, soy un {self.tipo} y mi sonido es el {self.onomatopeya}')

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

class Canario(Animal):
    tipo = 'canario'

class Conejo(Animal):
    tipo = 'conejo'

gato = Gato('kitty', 'maullido')
gato.saludo()

perro  = Perro('Chanchito', 'ladrido')
perro.saludo()

canario  = Canario('Piolin', 'silvido')
canario.saludo()

conejo = Conejo('Rabit', 'Ra')
conejo.saludo()
