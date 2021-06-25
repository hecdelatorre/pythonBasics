x = (1, 2, 3)
print(x)
print(type(x))

y = tuple((1, 2, 3))
print(y[1])

print(dir(tuple))

z = (1,) # Para una tupla de un elemento se coloca una coma
del z

locations = { # Diccionario con tuplas
    (35.12, 39.00): "Tokyo",
    (55.12, 39.00): "Kyoto"
}

print(locations)
print(type(locations))