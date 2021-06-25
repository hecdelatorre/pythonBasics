# Own modules
# Thirdy party modules

# python modules
import datetime
print(datetime.timedelta(minutes = 60))

from datetime import timedelta, date
print(timedelta(minutes = 990))
print(date.today())

# Mi modulo
import fmath
fmath.add(1, 2)
fmath.subtract(2, 1)

from fmath import add, subtract
add(4, 4)
subtract(3, 5)

# Modulos Pip -> pip install colorama
from colorama import Fore, Back, Style, init
# init(convert = True) # Para habilitar colores en windows cmd
print(Fore.RED + 'Hello World')

