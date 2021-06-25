demoList = [1, "hello", 1.3, True, [1,2,3]]
colors = ["red", "green", "blue"]
# colors.append("gray")
colors.extend(("gray", "yellow")) # Una tupla convierte en un solo elemento
colors.extend(["balck", "white"]) 
# Se usa extend para agregar multiples elementos

#colors.insert(-1, "pink")
colors.insert(len(colors), "pink")

print(colors)
colors[0] = "yellow"
colors.pop() # Remueve el ultimo elemento
colors.pop(1) # Quita el indice 1
colors.remove("gray")
print(colors)

print(f"La logitud de colores es: {len(colors)}")
print(colors[1])
print(colors[-1])
print(f"Verde disponible: {'green' in colors}")
print(f"Morado disponible: {'purple' in colors}")

colors.sort() # Ordena alfabeticamente
print(colors)
colors.sort(reverse = True) # Ordena de forma invessa
print(colors)
print(f"El indice de blue es: {colors.index('blue')}")
print(f"blue esta: {colors.count('blue')} vez")

colors.clear() # Quita toda la lista
print(colors)

numbersList = list((1,2,3,4)) # Se usa una tupla para crear una lista
print(type(numbersList))
print(numbersList)

r = list(range(1, 11))
print(r)


# print(f"\n{dir(r)}") # Muestra lo que es posible hacer con una lista