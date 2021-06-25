# import modulos as xs 
# 
# print(xs.mascotas)
# xs.saludo(xs.mascotas[2])

from camelcase import CamelCase
from modulos import saludo, mascotas
saludo(mascotas[1])

c = CamelCase()
s = 'esta oración necesita CamelCase'
o = 'Necesita camel case'
camelcased = c.hump(s)

print(camelcased)
print(c.hump(o))
