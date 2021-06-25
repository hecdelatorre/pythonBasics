import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

if os.path.exists('micarpeta'):
    os.rmdir('micarpeta')
else:
    print('La carpera no existe')

